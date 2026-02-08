INSERT INTO servers (ID, name, Motherboard, RAM, CPU, GPU, Disk) VALUES (NULL, 'SV1', 'ASUS', 'DDR4 2x16G 3200MHz', 'AMD ryzen 9 5800x', 'NVIDIA 3080 Ti', '4Tb');
INSERT INTO servers (ID, name, Motherboard, RAM, CPU, GPU, Disk) VALUES (NULL, 'SV2', 'ASUS', 'DDR4 2x16G 3200MHz', 'AMD ryzen 9 5800x', 'NVIDIA 3080 Ti', '4Tb');
INSERT INTO servers (ID, name, Motherboard, RAM, CPU, GPU, Disk) VALUES (NULL, 'SV3', 'ASUS', 'DDR4 2x16G 3200MHz', 'AMD ryzen 9 5800x', 'NVIDIA 3080 Ti', '4Tb');
INSERT INTO servers (ID, name, Motherboard, RAM, CPU, GPU, Disk) VALUES (NULL, 'SV4', 'ASUS', 'DDR4 2x16G 3200MHz', 'AMD ryzen 9 5800x', 'NVIDIA 3080 Ti', '4Tb');
INSERT INTO servers (ID, name, Motherboard, RAM, CPU, GPU, Disk) VALUES (NULL, 'SV5', 'ASUS', 'DDR4 2x16G 3200MHz', 'AMD ryzen 9 5800x', 'NVIDIA 3080 Ti', '4Tb');

INSERT INTO services (ID, services) VALUES (NULL, 'firewall');
INSERT INTO services (ID, services) VALUES (NULL, 'DNS');
INSERT INTO services (ID, services) VALUES (NULL, 'Web server');
INSERT INTO services (ID, services) VALUES (NULL, 'DB server');
INSERT INTO services (ID, services) VALUES (NULL, 'VPN');

INSERT INTO deployment (ID, server ID, service ID, date, status) VALUES (NULL, '1', '1', '2026-02-08', 'production');
INSERT INTO deployment (ID, server ID, service ID, date, status) VALUES (NULL, '1', '2', '2026-02-08', 'development');
INSERT INTO deployment (ID, server ID, service ID, date, status) VALUES (NULL, '4', '1', '2025-07-08', 'development');
INSERT INTO deployment (ID, server ID, service ID, date, status) VALUES (NULL, '3', '4', '2026-01-08', 'production');
INSERT INTO deployment (ID, server ID, service ID, date, status) VALUES (NULL, '5', '5', '2023-02-08', 'production');