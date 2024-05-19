# snippets

This repo has my (public) text expansion snippets.

Text expansion apps allow me to save keystrokes when I'm typing common words – for example, if I type `intl`, my computer expands it to `international`.
That saves me 9 keystrokes.
It may not seem like much, but I use these snippets dozens of times a day and it quickly adds up!

This repo has a script that creates a collection of snippets to use [in Alfred](https://www.alfredapp.com/help/features/snippets/).

## Motivation

I use a script rather than an in-app snippet editor because I want to share snippets between my home and work computers.

Most apps sync their preferences through some sort of cloud storage, e.g. Dropbox or iCloud.
I don't want to connect my home and work computers that way – I try to keep them separate.
e.g. I don't log into my work email on my home computer, and I don't log in to my personal iCloud on my work laptop.

By putting my snippets in a GitHub repo, I can check out the repo on both computers and get the same set of snippets, but in a way that maintains the gap between the machines.
Neither machine can directly affect the other.

I don't put all my snippets in this repo; just the ones I can make public.
For example, my home computer has extra snippets for personal info like my phone number and my address.
I configure those in the in-app editor, because I don't want to put them in a public Git repo and I don't need them on my work computer.

## Usage

```console
$ python3 create_snippets.py
```

This will create a new file `Alex’s snippets.alfredsnippets`, which you can open to add these snippets to Alfred Preferences.
