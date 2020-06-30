import sqlalchemy as sa

#Define conenction parameter
def connect():
    soch_engine = sa.create_engine('kylin://edward:Edward!123@qubz.dev-2.qubz-bi.com:80/CHAI_ICTC',connect_args={'is_ssl': False, 'timeout': 60})
    return soch_engine
