# yu-ssrp-azure-eip-smoketests-2022
A Repository to hold all smoke tests for YorkU SSRP's EIP on Azure for year 2022

## Smoke Tests: 
- [ ] Save credentials in keyvault 
- [ ] Build and deploy container image to ACR
- [ ] KeyVault is reachable from ACR
- [ ] Deploy Functions App from ACR
- [ ] Functions can read credentials from keyvault
- [ ] Function has inbound access from on-premises
- [ ] Function has inbound access from ssrpteam vpn
- [ ] Function has outbound internet access 
- [ ] Function can connect to a database on-premises (private network)
- [ ] Create service bus queue
- [ ] Service bus queue is reachable from on-premises (ssrpdeng1.eng)
- [ ] Service bus queue is reachable from ssrpteam vpn
- [ ] Service bus queue is reachable from functions in ASE 
- [ ] Deploye Self Hosted IR for data factory
- [ ] Self Hosted IR server can be RDP'd into from ssrpteam vpn
- [ ] Data factory can connect to on-premises database via self hosted IR (private network)
- [ ] Data factory can connect to dataverse via self hosted IR (outbound internet)
- [ ] Data factory can connect to blob storage in private network via self hosted IR
- [ ] Instanciate a container instance (docker run) from ACR
- [ ] Container instance has outbound internet access 
- [ ] Container instance can have mounted volume from private network