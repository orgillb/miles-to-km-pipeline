pipeline {
    agent any

    environment {
        CONDA_ENV = 'base'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/orgillb/miles-to-km-pipeline.git'
            }
        }

        stage('Setup Conda') {
            steps {
                bat 'call C:\\ProgramData\\anaconda3\\Scripts\\activate.bat'
                bat 'conda activate %CONDA_ENV%'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'coverage run -m unittest discover -s .'
                bat 'coverage report > coverage.txt'
                bat 'coverage html'
            }
        }

        stage('Build EXE') {
            steps {
                bat 'pyinstaller --onefile miles_to_km.py --name miles_to_km'
            }
        }

        stage('Package Installer') {
            steps {
                bat '"C:\\Program Files (x86)\\Inno Setup 6\\ISCC.exe" Installer.iss'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'dist/miles_to_km.exe, coverage.txt, Output/*.exe', fingerprint: true
            }
        }
    }
}
