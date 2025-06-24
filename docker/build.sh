pushd ../mealie-auto-tagger
VERSION=$(poetry version --short) docker buildx bake -f ../docker/docker-bake.hcl $@
popd