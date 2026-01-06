vim.opt.ignorecase = true
vim.opt.smartcase = true

vim.opt.number = true
vim.opt.cursorline = true
vim.opt.showmode = true

vim.opt.ignorecase = true
vim.opt.smartcase = true

vim.opt.clipboard = 'unnamedplus'
vim.opt.completeopt = {'menu', 'menuone', 'noselect'}
vim.opt.mouse = 'a'

vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.opt.smartindent = true

vim.opt.spelllang = 'en_us'
vim.opt.spell = true

vim.cmd('syntax enable')
vim.cmd('filetype plugin indent on')

vim.cmd('colorscheme elflord')
vim.cmd('hi SpellBad ctermbg=red')

require('save_as_root')

