class String(object):
    # link layer
    mac_addr_dst_ethernet_ii = 'mac_addr_dst'
    mac_addr_src_ethernet_ii = 'mac_addr_src'
    type_ethernet_ii = 'type_ethernet'
    data_payload = 'data_payload'

    ipv4 = 'IPv4'
    arp = 'ARP'
    rarp = 'RARP'
    ipv6 = 'IPv6'

    # mainly network layer
    ip_version = 'ip_version'
    length_header = 'length_header'
    type_service = 'type_service'
    length_total_packet = 'length_total_packet'
    id_packet = 'id_packet'
    flags = 'flags'
    offset_fragment = 'offset_fragment'
    time_to_live = 'time_to_live'
    id_protocol = 'id_protocol'
    checksum = 'checksum'
    ip_addr_src = 'ip_addr_src'
    ip_addr_dst = 'ip_addr_dst'
    # data_payload = 'data_payload'

    tcp = 'TCP'
    udp = 'UDP'

    class_traffic = 'class_traffic'
    label_flow = 'label_flow'
    length_payload = 'length_payload'
    header_next = 'header_next'
    limit_hop = 'limit_hop'
    # ip_addr_src = 'ip_addr_src'
    # ip_addr_dst = 'ip_addr_dst'
    # data_payload = 'data_payload'

    # transport layer
    port_src = 'port_src'
    port_dst = 'port_dst'
    sequence_first_byte = 'sequence_first_byte'
    sequence_acknowledgement = 'sequence_acknowledgement'
    # length_header = 'length_header'
    reserved = 'reserved'
    # flags = 'flags'
    size_window = 'size_window'
    # checksum='checksum'
    pointer_urgent = 'pointer_urgent'
    # data_payload = 'data_payload'
