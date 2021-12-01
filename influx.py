import pandas as pd
from influxdb_client import InfluxDBClient
 
client = InfluxDBClient(url="http://localhost:8086", token="J7VCW1JAk9PICJNH68fNqoU-wdTIR7j6xATlSgwxFo_DQX2-0A4QKwFRSEZvAs7ubIZQzxCPWkEXUhekWsNpnQ==", org="myorg")
write_client = client.write_api()
 
df = pd.read_csv("강서구.csv")
df.rename(columns={'측정일시':'_time'},inplace=True)
df['_time'].astype(int) 
df['_time'] = pd.to_datetime(df['_time'], format="%Y-%m-%dT%H:%M:%SZ")
df.set_index(['_time'])

 
write_client.write("asd", "anais@influxdata.com", record=df, data_frame_measurement_name="_measurement",
                           data_frame_tag_columns=['region', 'host'])