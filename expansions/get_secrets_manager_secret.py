def get_secret_string(sess: boto3.Session, **kwargs) -> str:
    """
    Look up a SecretString from Secrets Manager, and return the string.
    """
    secrets = sess.client("secretsmanager")

    resp = secrets.get_secret_value(**kwargs)

    return resp["SecretString"]
