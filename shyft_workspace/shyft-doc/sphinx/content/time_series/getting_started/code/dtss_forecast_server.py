import argparse
from pathlib import Path
from shyft.api import DtsServer
from time import sleep

def start_server(port:int, dtss_dir:str, max_items:int):
    s=DtsServer()
    s.set_listening_port(port)
    s.cache_max_items=max_items  # approx 3 Gpts, 24 GB of cache with 66hour fc. timeseries
    s.set_container('forecast',dtss_dir)
    s.start_async()
    return s

def print_stats(s):
    while True:
        sleep(5)
        c=s.cache_stats
        print(f'hits {c.hits} misses {c.misses} id_count {c.id_count} # {c.point_count/1e6} Mpts')


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description='Start a dtss server for testing')
    parser.add_argument('--port_no',type=int,default=20000,help='port number(default 20000) to use, typicall range 10000..50000')
    parser.add_argument('--cache_max_ts',type=int,default=50*1000000,help='maximum # (default 50 mill) of ts to keep in lru-cache')
    parser.add_argument('--dtss_root_dir',type=str,help='absolute path to the root directory for the shyft dtss ts-containers, like $HOME/dtss_root')
    a=parser.parse_args()
    fc=Path(a.dtss_root_dir)/'forecast'
    if not fc.exists():
        fc.mkdir()
    s=start_server(port=a.port_no,dtss_dir=str(fc),max_items=a.cache_max_ts)
    print(f'dtss is started on local port {s.get_listening_port()}')
    print(f'- dtss_root is {a.dtss_root_dir}, max-ts in cache set to {a.cache_max_ts}')
    print('ctrl-C to terminate')
    try:
        print_stats(s)
    except :
        print('terminated')
        s.clear()
    print('done')
