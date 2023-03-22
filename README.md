```console
/tmp $ git clone git@github.com:gabrielhora/pants_17403.git
Cloning into 'pants_17403'...
remote: Enumerating objects: 20, done.
remote: Counting objects: 100% (20/20), done.
remote: Compressing objects: 100% (14/14), done.
Receiving objects: 100% (20/20), 8.29 KiB | 8.29 MiB/s, done.
remote: Total 20 (delta 0), reused 20 (delta 0), pack-reused 0

/tmp $ cd pants_17403

/tmp/pants_17403 $ ./pants fmt lint ::
10:42:31.84 [INFO] Initializing scheduler...
10:42:32.60 [INFO] Scheduler initialized.
10:42:35.69 [INFO] Completed: Format with isort - isort made no changes.
10:42:35.69 [INFO] Completed: Format with isort - isort made no changes.

✓ isort made no changes.
10:42:35.70 [WARN] Completed: Format with isort - isort made changes.
  src/project/main.py

✕ isort failed.

(One or more formatters failed. Run `./pants fmt` to fix.)
```