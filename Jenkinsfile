pipeline {
        agent any
        stages {
                parallel {
                        stage('Build Phase') {
                                steps {
                                        echo 'Build phase completed'
                                }
                        }
			stage('Testing Phase') {
				steps {
					echo 'Testing phase comepleted'
				}
			}
                        stage('Deployment Phase') {
                                steps {
                                        echo 'Deployment completed'
                                }
                        }
                }
        }    
                
}


