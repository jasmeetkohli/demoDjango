env.cron_string = BRANCH_NAME == "dev" ? "*/1 * * * *" : ""
env.app = "test"
env.app_name = "demo-" + app
env.secret = credentials('secret_test')
env.some_var = application_name + "-test"

pipeline{
    agent any
    triggers { pollSCM(cron_string) }
    /*parameters {
        choice(name: 'ENVIRONMENT', defaultValue: 'development', choices: ['development\nstaging\nproduction'])
        choice(name: 'APPLICATION', defaultValue: 'kaarmana-auth', choices: ['kaarmana-auth\nlotus-auth'])
    }*/
    parameters {
        choice(
            name: 'application_name',
            choices: "demo_1\ndemo_2",
            description: 'interesting stuff' )
    }  
    environment {
        namespace = 'kaarmana-dev'
        secret_text = credentails('secret_test')
    }
    stages{
        stage("Build"){
            //agent {label 'build_PROD'}
            steps{
                //script {
                    //String some_var = application_name + "-test"
                //}
                sh '''
                    echo "${secret}"
                    echo "${secret}" > mysecret
                    cat mysecret
                    rm mysecret
                    echo "${secret_text}"
                    echo "${secret_text}" > mysecret
                    cat mysecret
                    rm mysecret
                    echo "application: ${application_name}"
                    echo "some_var: ${some_var}"
                    echo "app_name: ${app_name}"
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
