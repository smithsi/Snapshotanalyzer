# Snapshotanalyzer 
Demo project to manage AWS EC2 instance snapshots

## About
This project is a demo & uses boto3 to manage AWS EC2 instances

## Configuration
Shotty uses the configuration file created by AWS CLI

'aws configure --profile shotty'

## Running
Run shotty 

`pipenv run python snapshotanalyzer/shotty.py <command> <subcommand ><--project=PROJECT>"`

*command* is instances, volumes or snapshot
*subcommand* - depends on command
*project* is optional