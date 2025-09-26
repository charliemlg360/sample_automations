How this works:

remy_dinner_deploy calls the following python scripts in this order:

remy_pasta2: the main script used to download your list of CRLs plus your crl.zip from crl_urls.

remy_unpack: unzips your crl.zip file and then deletes the archive.

remy_delivery: copies your crl files into your exeternal drive.


After you transfer your files over from your external drive, you can run CRL Upload onto your air gapped system to put them in the correct directory for your applications.

When you're done run remy_cleanup to remove your old crls from your external drive and local system.
