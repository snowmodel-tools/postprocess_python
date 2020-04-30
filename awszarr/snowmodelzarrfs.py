'''
NOTES

Warning: The statement FS = s3fs.S3FileSystem(session=aws_session) below is failing when using s3fs version 0.4.2 
(current version on conda-forge, 4/4/2020) and boto3 1.12.35 and 1.12.36. 
But it does work when using s3fs 0.4.0 and boto3 1.12.27.

Exploring read-only access. Compare https://snowmodel.s3.us-west-2.amazonaws.com and https://snowmodel.s3.us-west-2.amazonaws.com/swe_gdat_1.zarr/.zattrs (produces AccessDenied) to https://io2data.s3.us-west-2.amazonaws.com/ and https://io2data.s3.us-west-2.amazonaws.com/data/CE02SHBP-LJ01D-06-CTDBPN106-streamed-ctdbp_no_sample/20160428/.zattrs (the file can be downloaded)

When passing an AWS profile under fs_type == 'aws_s3', an AWS credentials file in the default location 
(on Linux and Macs, it's `~/.aws/credentials`) is required. The file must have these entries:
  [cso]
  aws_access_key_id=CSO_ACCESS_KEY_ID
  aws_secret_access_key=CSO_SECRET_ACCESS_KEY
Where `CSO_ACCESS_KEY_ID` and `CSO_SECRET_ACCESS_KEY` are the required CSO keys.
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#shared-credentials-file
'''


from pathlib import Path

import s3fs
import boto3


def connect_fs(fs_type, aws_profile_name=None):
    """
    fs_type: localfs, localminio_s3, aws_s3, or anon_aws_s3
    """
    if fs_type == 'localfs':
        fs = None
    elif fs_type == 'localminio_s3':
        fs = s3fs.S3FileSystem(
            key='minioadmin',
            secret='minioadmin',
            client_kwargs={"endpoint_url": "http://172.17.0.2:9000"}
        )
    elif fs_type == 'aws_s3':
        # Use stored credentials file, ~/.aws/credentials
        # Can also pass the credentials here explicitly via parameters
        # aws_access_key_id and aws_secret_access_key, but that's not safe
        aws_session = boto3.Session(
            profile_name=aws_profile_name,
            aws_session_token=None,
            region_name='us-west-2'
        )
        fs = s3fs.S3FileSystem(session=aws_session)
    elif fs_type == 'anon_aws_s3':
        fs = s3fs.S3FileSystem(anon=True)
    
    return fs


def get_zarrstore(fs, fs_type, bucket, zarrds, base_dpth=None):
    """
    zarrds is the relative path below the bucket, to the zarr dataset object. 
    In the examples below, zarrds is the string below "<bucket>/"
    <bucket>/mydataset.zarr
    <bucket>/mydir/mydataset.zarr
    """
    if fs_type == 'localfs':
        # Looks like `open_zarr` doesn't accept pathlib Paths, so convert to str
        zarrstore = str(Path(base_dpth) / bucket / zarrds)
    elif fs_type.endswith('s3'):
        zarrstore = s3fs.S3Map(f"{bucket}/{zarrds}", s3=fs)
    
    return zarrstore
                                                                         