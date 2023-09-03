### Please note this project is under heavy development. Expect sudden and breaking changes

# Introduction

High Dimensional Research let agents use the internet. The internet was built for people, so HDR is creating tools to let agents browse, use, and learn from the internet. Our search engine and browser are powered by a global vector cache.

Why this rules:

1. **Cheaper**: The internet has over 120 zettabytes of information on it. We only embedd when pages change to save everyone a boat load of cash.
2. **Faster**: Can't beat a cache.
3. **Better**: Our embeddings are top notch since it is literally all we think about. We also leverage accessibility tooling and other neat tricks to isolate the important information of the internet.
4. **Greener**: GPUs use a lot of power. We save your wallet and the planet by creating an information commons.

If you have any questions, please email [Tynan Daly](mailto:tynan.daly@hdr.is)

## FAQ

> Is this yet another vector database?

No! HDR uses a new kind of vector index construction algorithm based on algebraic toplogy (we know, we can't believe an application actually exists either) to efficiently run vector search on the public internet. However, this means that we do not run search over your private documents. Go talk to our friends over at Pinecone, Milvus, or Chroma for that and let them know we sent you!

> What can I do with this?

Most people use the search function to help their agents navigate the internet and then switch over to the browser when the agents find what they're looking for.

Give them poetry, financial documents, real time news, etc. Run rag. Summarize text. Search for images (soon). Finally stop worrying about that damn training cutoff date.

> How do I singup? I dont see anything on your website.

Join the waitlist and if you really need this, email [Tynan](mailto:tynan.daly@hdrl.is) to get bumped up.

> Are my searches private?

No. We use search results to reweight the search indexes and (soon) customize them to your agents. Besides, we someone has to make sure the robots behave.

> Do you have a discord?

No!

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
