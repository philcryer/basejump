* setup time for Alpine Linux

# Set timezone
ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime

# Install and start time sync
apk add chrony
rc-service chronyd start
rc-update add chronyd

# Check result
date
