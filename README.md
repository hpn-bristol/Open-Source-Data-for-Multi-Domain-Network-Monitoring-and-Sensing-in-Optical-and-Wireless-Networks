# Open-Source-Data-for-Multi-Domain-Network-Optimisation-and-Sensing-in-Optical-Networks-and-WANs

## One-month Performance Monitoring Data from Optical Transport Network over NDFF

## Two-week Sensing Data from BDFI and Mshed

## Wireless Access Network Dataset

This dataset is collected from a multiple radio access technologies testbed, the network architecture is as the figure shown.

```mermaid
graph LR
   CPE1 <--> 5G
   CPE1 <--> WiFi
   CPE2 <--> 5G
   CPE2 <--> WiFi
   CPE3 <--> 5G
   CPE3 <--> WiFi
   CPE4 <--> 5G
   CPE4 <--> WiFi
   CPE4 <--> LiFi
   5G <--> Network
   WiFi <--> Network
   LiFi <--> Network
```

There are four CPEs in the network. CPE1,CPE2,CPE3 are connected to both 5G and WIFI access point. CPE4 is connected to 5G ,WIFI and Lifi access point. MPTCP is enabled in all CPEs. 

The MPTCP path manager is fullmesh: it will try to create an additional subflow for each known peer address, using this endpoint as the source IP address. And the MPTCP implements a simplified version of the BLEST algorithm as its scheduler, trying to avoid HoL blocking. It sends as much as possible over the active path, before using the others. 

Traffic is transmitted from CPE1,CPE2,CPE3 to CPE4 using iperf with MPTCP enabled. And the dataset contains the parameters recored in all access points and all CPEs during the transmission.

### MAC Address and Interface for Each CPE
| CPE | Wifi MAC Address      | Lifi MAC Address      | 5G Interface | Wifi Interface      | Lifi Interface       |
| --- | --------------------- | --------------------- | ------------ | ------------------- | -------------------- |
| 1   | c8:3a:35:a0:05:fd      | None                  | wwan0        | wlxc83a35a005fd      | None                 |
| 2   | c8:3a:35:a4:07:0d      | None                  | wwan0        | wlxc83a35a4070d      | None                 |
| 3   | c8:3a:35:ac:04:5d      | None                  | wwan0        | wlxc83a35ac045d      | None                 |
| 4   | c8:3a:35:a4:06:9d      | 00:c0:ca:b5:c6:77     | wwan0        | wlxc83a35a4069d      | wlx00c0cab5c677       |

A [24-hour dataset](https://github.com/hpn-bristol/Open-Source-Data-for-Multi-Domain-Network-Optimisation-and-Sensing-in-Optical-Networks-and-WANs/tree/main/WAN_24h) including the raw data and processed data is generated. For your infomation, we also provide the [raw data preprocessing code](https://github.com/hpn-bristol/Open-Source-Data-for-Multi-Domain-Network-Optimisation-and-Sensing-in-Optical-Networks-and-WANs/blob/main/WAN_24h/process_data.ipynb).

### Parameters Included in Dataset

#### 1. CPE Data

CPEs Included: CPE1, CPE2, CPE3, CPE4

Each CPE file includes the following metrics:
- `recv [interface]`: Data received on specified interface
- `trans [interface]`: Data transmitted on specified interface

#### 2. 5G Cell Data

The 5G cell dataset encompasses:
- **Temperature Sensor Readings**: Monitors the temperature of the 5G cell equipment.
- **Uplink/Downlink Throughput Measurements**: Measures the data throughput in both uplink and downlink directions.
- **RMOD Power**: Reflects the power consumption or output in the Radio Modulation units.

#### 3. LiFi Cell Data

Data concerning LiFi technology includes:
- **Transmitted (Tx) / Received (Rx) Bitrates**: Measures the bitrates transmitted to and received from each CPE by the LiFi access point, identified by MAC address.
- **Signal Power**: Indicates the power of the signal at the LiFi access point for various CPEs.

#### 4. WiFi Cell Data

WiFi data metrics are as follows:
- **Inactivity Time**: Tracks the periods of inactivity of each CPE.
- **Transmitted (Tx) / Received (Rx) Bitrates**: Documents the bitrates that the WiFi access point transmits to and receives from each CPE, identified by MAC address.
- **Signal Averages**: Captures the average signal levels at the WiFi access point for different CPEs.

#### Additional Notes:
- Each file in LiFi and WiFi cell data corresponds to a specific CPE, identified by MAC address. The data is presented from the perspective of the access points, such as the amount of data transmitted to and received from each CPE by the access points, and the signal strength detected for each CPE at the access points.

## Contact Information
Author: 
- Sen Shen
- Xueqing Zhou [xueqing.zhou@bristol.ac.uk](mailto:xueqing.zhou@bristol.ac.uk)
- Wanxin Zhao

Feel free to contact us if you have any questions regarding the dataset.
