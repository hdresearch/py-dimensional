### Please note this project is under heavy development. Expect sudden and breaking changes

# Introduction

High Dimensional Research let agents use the internet. HDR is creating tools to let your agents browse, use, and learn from the internet. We provide a global vector cache, a vector search engine, and a browser for you and your agents to use.

## Usage

Please grab an api key from [hdr.is](https://hdr.is). Then either add it to your `.env` file or export it to your favorite shell via `export HDR_API_KEY=your-api-key-here`.

Clone the repo

```sh
git clone git@github.com:hdresearch/py-dimensional.git
```

Navigate to the directory

```sh
cd py-dimensional
```

Install `py-dimensional`

```
pip3 install .
```

Run examples

```sh
python examples/rag.py
python examples/summarize.py
```

## Contribution

If you would like to contribute to this project:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Testing

We use poetry for development :)

```bash
poetry install --with dev
pytest
```
