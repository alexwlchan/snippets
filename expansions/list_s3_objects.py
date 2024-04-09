def list_s3_objects(sess: boto3.Session, **kwargs):
    s3 = sess.client("s3")

    for page in s3.get_paginator("list_objects_v2").paginate(**kwargs):
        yield from page.get("Contents", [])
