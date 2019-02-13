String cron_string = BRANCH_NAME == "dev" ? "*/1 * * * *" : ""

pipeline{
    agent any
    triggers { pollSCM(cron_string) }
    /*parameters {
        choice(name: 'ENVIRONMENT', defaultValue: 'development', choices: ['development\nstaging\nproduction'])
        choice(name: 'APPLICATION', defaultValue: 'kaarmana-auth', choices: ['kaarmana-auth\nlotus-auth'])
    }*/
    environment {
        namespace = 'kaarmana-dev'
    }
    stages{
    
        stage("Build"){
            //agent {label 'build_PROD'}
            steps{
                sh '''
                    echo "BRANCH: ${BRANCH_NAME}"
                    echo "############################################"
                    env
                    echo "From DEV"
                    #ls -aRl
                '''
            }    
        }
    }
}
