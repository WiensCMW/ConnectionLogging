# ConnectionLogging
Simple python scripts that continuously pings specified hostnames, and if it fails to ping any of them it logs the results.

The script will first attempt to ping the router, if that succeeds it will ping the hostnames in the list_list array. If the ping succeeds for any of the hostnames in that array the script sleeps 3 seconds before starting again, it does not log successful pings. If the ping to the router is successful but it can't ping any of the hostnames in the array it will log the datetime to a text file.
