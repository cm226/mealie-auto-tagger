variable "VERSION" {
  default = "latest"
}

group "default" {
  targets = ["meaile-auto-tagger"]
}

target "meaile-auto-tagger" {
  context    = "../"
  dockerfile = "./docker/Dockerfile"
  tags       = ["cm226/mealie-auto-tagger:${VERSION}"]
}