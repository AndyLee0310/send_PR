# send PR

We use [Github REST API](https://docs.github.com/en/rest) to help send PR

## Instructions

At the `send_PR.py`,

1. user's auth token need to be changed to your token
    ```python
    auth_token = "user's auth_token"
    ```

2. repositorie's owner need to be changed to the owner of the repositorie want to send PR
    ```python
    owner = "repositorie's owner"
    ```

3. repositorie name need to be changed to the repositorie where you want to send PR
    ```python
    repo = "repositorie name"
    ```

4. reviewers need to be changed to the list of one or more people you want to join
    ```python
    reviewers = ["reviewers"]
    ```

5. assignees need to be changed to the list of one or more people you want to join
    ```python
    assignees = ["assignees"]
    ```

6. labels need to be changed to the list of one or more people you want to join
    ```python
    labels = ["labels"]
    ```

**If you don't need reviewers, assignees, and labels, you must remove lines 28-31 and lines 46-77 in `send_PR.py`**

## Note

You need to get your account token to access the pull request's operations.

## License

This project is [GNU General Public License 3.0](https://www.gnu.org/licenses/gpl-3.0.html) licensed.