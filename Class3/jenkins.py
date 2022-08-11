/home/lederman/Desktop
sudo sh -c 'echo "Noam Lederman" >> fileName'
properties([pipelineTriggers([cron('H * * * *')])])
node("new-noam"){
    stage("one"){
        echo "Print Name: Noam Lederman"
    }
    stage("two"){
        sh cd /home/lederman/Desktop
        sh 'echo "Noam Lederman" >> fileName'
    }
}

