# See 

### [Masonite + postgres](https://testdriven.io/blog/dockerizing-masonite-with-postgres-gunicorn-and-nginx/#:~:text=$%20mkdir%20masonite%2Don%2Ddocker,dev.)

### [AlloyDB](https://www.google.com/search?q=AlloyDB+image+for+tests+docker-compose&sca_esv=fb973f3e0fcee097&ei=eI_vaIvxH5f97_UPh5OqsQM&ved=0ahUKEwiLjcO3lqaQAxWX_rsIHYeJKjYQ4dUDCBA&uact=5&oq=AlloyDB+image+for+tests+docker-compose&gs_lp=Egxnd3Mtd2l6LXNlcnAiJkFsbG95REIgaW1hZ2UgZm9yIHRlc3RzIGRvY2tlci1jb21wb3NlMgcQIRgKGKABMgcQIRgKGKABSOYTUL4GWNcScAF4AZABAJgB-AGgAZMLqgEFMC41LjK4AQPIAQD4AQGYAgigArULwgIKEAAYRxjWBBiwA8ICBRAhGKABmAMAiAYBkAYEkgcFMS40LjOgB-AOsgcFMC40LjO4B7ALwgcFMS42LjHIBw4&sclient=gws-wiz-serp)

```
version: '3.8'
services:
  alloydb-omni:
    image: google/alloydbomni:16.3.0 # Use the desired image tag, e.g., 16.3.0 or 16.3.0-ubi
    container_name: my-alloydb-omni-test
    environment:
      POSTGRES_PASSWORD: your_strong_password # Replace with a strong password
    ports:
      - "5432:5432" # Map the container's PostgreSQL port to the host
    volumes:
      - alloydb_data:/var/lib/postgresql/data # Mount a named volume for persistent data
    ulimits:
      nice: -20:-20 # Recommended for optimal performance
      memlock: -1:-1 # Recommended for optimal performance
volumes:
  alloydb_data:
```
