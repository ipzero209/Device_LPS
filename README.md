# Device_LPS
Used to estimate logging rate based on log receiver statistics.

This set of scripts will poll the firewall to see how many logs are written per second. It pulls the lps value from the 'debug log-receiver statistics" command and is intended to provide an estimate of the number of logs per second that can be forwarded from the device. Note that the number will be accurate provided all policies are configured to forward logs.


Usage:

"/usr/bin/expect /home/myuser/device_lps.exp Firewall_IP username device_type Number_of_samples"

- device_type can be either 'fw' or 'cms'. 'fw' will send the appropriate command for a firewall while 'cms' will send the appropriate command for Panorama.
- Samples are taken every 10 seconds, so you would enter 360 to get samples over an hour.

This is still a work in progress. If you have any issues, please reach out to cstancill@paloaltonetworks.com.
