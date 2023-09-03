import speedtest

st = speedtest.Speedtest()
def get_servers():
    return st.get_servers()


def test_speed(server):

    st.get_best_server()
    download_speed = st.download() / 10**6
    upload_speed = st.upload() / 10**6

    return download_speed, upload_speed

servers=get_servers()
print(servers)
down,up=test_speed(st.get_best_server)
print(down,up)
