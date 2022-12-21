resource "aws_ecr_repository" "cad-event-scraper" {
    name = var.ecr_name
    image_tag_mutability = var.image_mutability
    tags = var.tags
}