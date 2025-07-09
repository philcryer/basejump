local function save_as_root(opts)
    local tool = nil

    -- On Alpine Linux, we use doas. However, make this code work on any Linux
    -- distribution by also supporing sudo. Figure out which one we have,
    -- favoring doas if both are installed.
    if vim.system({'which', 'doas'}):wait().code == 0 then
        tool = 'doas'
    elseif vim.system({'which', 'sudo'}):wait().code == 0 then
        tool = 'sudo'
    end

    -- If neither doas nor sudo are available, return since we can't do anything
    if not tool then
        print('Error: neither doas nor sudo is available')
        return
    end

    local output = ''

    -- We now define a function inside a function (an example of a closure) that lets
    -- us detect if doas/sudo asks for a password. If it asks, we ask the user to
    -- enter their password using vim.fn.inputsecret in order to obscure it. We then
    -- send that password over to doas/sudo to authenticate.
    local function handle_stdout(channel_id, data, name)
        if #data > 0 then
            if data[1]:find('password') then
                local password = vim.fn.inputsecret('(' .. tool .. ') password: ')
                vim.fn.chansend(channel_id, { password, '' })
            else
                output = output .. data[1]:gsub('\r', '\n')
            end
        end
    end

    -- Create a temporary file by getting a temporary filename and writing the contents
    -- of our buffer to it.
    local temp_file = vim.fn.tempname()
    vim.cmd.write(temp_file)

    -- Although we might not use it often, :w supports "save as" functionality by letting
    -- us specify an alternate filename as an argument. We can support the same thing
    -- for :W by picking up the argument.
    local ebang = true
    local filename = vim.api.nvim_buf_get_name(0)
    if opts.args ~= '' then
        ebang = false
        filename = opts.args
    end

    -- Both doas and sudo expect to be running directly in a terminal emulator
    -- (either an actual tty or a pseudoterminal [pty]). Neither command is
    -- happy with basic input redirection, so we have to use the following
    -- construct. What we're doing is using doas/sudo to copy our temporary file
    -- to our original file. We could use the cp command here, but to avoid the
    -- risk of shell differences, we use dd instead.
    local channel_id = vim.fn.jobstart({tool, 'dd', 'if=' .. temp_file, 'of=' .. filename}, {
        on_stdout = handle_stdout,
        pty = true,
    })

    if vim.fn.jobwait({channel_id})[1] == 0 then
        -- Success: reload the buffer and clear the modified flag, unless we saved using an
        -- alternate filename
        if ebang then
            vim.cmd('e!')
        end

        vim.cmd('redraw')
        vim.print('Written (as root): ' .. filename)
    else
        -- Something went wrong, so display the error message in the status line
        vim.print(output)
    end

    -- Clean up the temporary file
    vim.fn.delete(temp_file)
end

vim.api.nvim_create_user_command('W', save_as_root, {desc = 'Save file as root', nargs = '?'})

