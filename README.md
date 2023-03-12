# Future data platform (FDP)
The successor to the MDP, mistakes were made, may our children forgive us. A more detailed view of the azure landscape and development practices can be found here in our [Azure & Devops process](deployment/README.md). In lieu of the previous carnage, we are sticking to a much simpler, industry standard approach, losely based on this [sample pyspark project](https://github.com/AlexIoannides/pyspark-example-project) for a Python / Spark / Databricks / Prefect solution.
<br/>
<br/>

## Setup
The guide below will hopefully give a little nudge for how to get going in running this locally. Good idea to turn off Global Protect (💩💩) when working as it will improve performance by about 3000%. **Also commands need to be run as admin**. In honesty given the restrictions on these machines I'd be inclined to work from VMs (or Macs 😛) but I guess these bring their own issues.
<br/>
<br/>

### Pre-requisites
___
<br/>

1. [Install chocolatey](https://docs.chocolatey.org/en-us/choco/setup)
2. choco install python --version=3.7.7
3. choco install vscode (Be cool 😎*)
4. choco install gow (windows only)
5. choco install jdk8 (windows only)
6. [Download the latest Hadoop utils](https://github.com/kontext-tech/winutils) to c:\Hadoop\bin (windows only)
7. Run powershell below to set the Hadoop home env variable (windows only)
```powershell
[System.Environment]::SetEnvironmentVariable('HADOOP_HOME','c:\Hadoop',[System.EnvironmentVariableTarget]::Machine)
[System.Environment]::SetEnvironmentVariable("Path", [System.Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::Machine) + ";%HADOOP_HOME%\bin",[EnvironmentVariableTarget]::Machine)
```
8. Restart vscode (if open)
9. Create a .env file at the root of your solution for configuring Databricks connect
```
DEBUG=1
PYTHONPATH=.
PYSPARK_PYTHON=[[your venv path]]\Scripts\python.exe
SPARK_HOME=[[your venv path]]\lib\site-packages\pyspark
PREFECT__CONTEXT__SECRETS__DATABRICKS_CONNECTION_STRING={"host":"[[cluster host]]","token":"[[cluster token]]"}
PREFECT__CLOUD__AGENT__AUTH_TOKEN=l2K1u9Vs4Fxvz95s9ETOtQ
DATABRICKS_HOST=[[cluster host]]
DATABRICKS_TOKEN=[[cluster token]]
DATABRICKS_CLUSTER_ID=[[cluster id]]
AZURE_STORAGE_CONNECTION_STRING=[[shared storage connection]]
MOUNT=dbfs:/mnt/sandboxes/[[env name]]/
ENVIRONMENT=sandboxes
RELEASE_VERSION=[[version && your name]]
APP_IMAGE=prefecthq/prefect:latest-python3.7
```
10. Run bash ./scripts/setup.sh in **bash** from the vscode terminal

<details>
<summary>* Install vscode extensions 😎</summary>

___
```
basarat.god
esbenp.prettier-vscode
hashicorp.terraform
hbenl.vscode-test-explorer
hediet.vscode-drawio
hediet.vscode-drawio-insiders-build     
humao.rest-client
KevinRose.vsc-python-indent
littlefoxteam.vscode-python-test-adapter
ms-azure-devops.azure-pipelines
ms-azuretools.vscode-apimanagement      
ms-azuretools.vscode-azurefunctions     
ms-azuretools.vscode-azureresourcegroups
ms-azuretools.vscode-azureterraform    
ms-python.python
ms-python.vscode-pylance
ms-toolsai.jupyter
ms-vscode.azure-account
ms-vscode.powershell
njpwerner.autodocstring
oderwat.indent-rainbow
redhat.vscode-commons
redhat.vscode-yaml
shd101wyy.markdown-preview-enhanced
streetsidesoftware.code-spell-checker
TabNine.tabnine-vscode
ukoloff.win-ca
yzhang.markdown-all-in-one
```
</details>
<br/>

##  Developing
So, you want to be able to connect your IDE up to Databricks when working on your PR but you also you want to be able to develop locally so you can not cost the company $$$ and develop faster. Well fear no more, for alas this is possible with the FDP. 
<br/>
<br/>

### Databricks CLI
___
<br />

We no longer make use of databricks-connect and instead use the databricks CLI. This means we need to package up the code and deploy it to the dbfs before triggering a job locally with prefect. We currently have two scripts to do this:

* pipenv run package
* pipenv run deploy

Then to run a flow, you can simply call:

* pipenv run python [[path to flow]]

You could also alternatively just kick off your spark job against a local cluster or run it as part of a unit test, up to you as long as you have scaffolded out your local hive metastore data.
<br/>
<br/>

### Weirdness
___
<br />

* First rule of FDP is, never use Global Protect.
* Second rule of FDP is, never use Global Protect.
* If you are setting up on OSX, then you may be best installing installing pyenv and globally setting your python version to be 3.7.*. 
* [Python not found on vscode on windows](https://www.reddit.com/r/vscode/comments/duxqtq/python_was_not_found_but_can_be_installed_from/)

### Known Issues/Todo
___
<br />

* Unused agents are not cleaned up - _mitaged manually, mitigation can be automated_
* Send AKS logs to log analytics and azure monitor - _not mitigated, mitigation can be automated_
* Service account to trigger Azure pipeline PR complete or abandon (requires Barry) - _mitaged manually, mitigation can be automated_: **Speak to infra**
