mv Dockerfile Dockerfile.main
mv Dockerfile.test Dockerfile

mv docker-compose.yml docker-compose.yml.main
mv docker-compose.yml.test docker-compose.yml

echo "Entered testing mode, make sure to switch back before making any commits"
