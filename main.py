from module.dataProcessing import nameClass


def defining_classes(ip):
    first_index = (ip)  # receive list type
    ip_class = ''

    return nameClass(first_index, ip_class)


def calculate_subnet_mask(ip):
    ip = defining_classes(ip)

    class_ipv4 = [
        {'A': '255.0.0.0'},
        {'B': '255.255.0.0'},
        {'C': '255.255.255.0'},
    ]

    for index in class_ipv4:
        ip_class = list(index.keys())[0]
        subnet_mask = list(index.values())[0]

        if ip == ip_class:
            return subnet_mask

    return "non-resulting mask number"


ipv4 = input('Type the IPv4: ').split('.')

print(ipv4, defining_classes(ipv4))
print(calculate_subnet_mask(ipv4))


# TO SEND A WHOLE LIST / SEVERAL IPS AT THE SAME TIME
# list_ip = [
#     ['192.168.0.10'],
#     ['10.0.0.254'],
#     ['172.16.20.100'],
#     ['203.0.113.55'],
#     ['198.51.100.22'],
#     ['172.20.0.1'],
#     ['192.0.2.50'],
#     ['10.10.5.100'],
#     ['198.18.0.22'],
#     ['203.0.113.99'],
#     ['192.168.1.20'],
#     ['172.31.0.5'],
#     ['10.20.30.40'],
#     ['255.51.100.77'],
#     ['192.168.10.15']
# ]

# for indice in list_ip:
#     primeiro_elemento = indice[0]
#     primeiro_valor = primeiro_elemento.split('.')
#     print(indice, defining_classes(primeiro_valor))


# exemplos:
# 192.168.0.10
# 10.0.0.254
# 172.16.20.100
# 203.0.113.55
# 198.51.100.22
