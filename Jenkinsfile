pipeline{
    agent any
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
                sh 'echo "From DEV"'
            }    
        }
    }
}
