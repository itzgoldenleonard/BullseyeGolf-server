mv Dockerfile Dockerfile.test
mv Dockerfile.main Dockerfile

mv docker-compose.yml docker-compose.yml.test
mv docker-compose.yml.main docker-compose.yml

echo "Entered production mode, you can now safely commit"

