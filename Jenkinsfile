pipeline {
        agent any
        stages {
		stage('Run Test') {
			parallel {
				stage('Build Phase') {
					agent {
						docker { image 'alpine:20181019' }	
					}		
					steps {
						sh '''echo Build phase completed '''
					}
				}
				stage('Testing Phase') {
					agent {
						docker { image 'alpine:20181019' }	
					}
					steps {
						sh '''echo Testing phase comepleted'''
					}
				}
				stage('Deployment Phase') {
					agent {
						docker { image 'alpine:20181019' }	
					}
					steps {
						sh '''echo Deployment completed'''
					}
				}
			}
		}
        }    
                
}


