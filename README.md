# travis-build-repeat
>👷  Repeat TravisCI builds to avoid stale test results

If your project's tests rely on a 3rd party API or service, running your tests at commit time isn't enough. To ensure your projects continue function correctly, you need to regularly run your test suite. `travis-build-repeat` lets you automate this process with [AWS Lambda](https://aws.amazon.com/lambda/).

Once setup, `travis-build-repeat` automatically restarts the latest build of your project on a schedule, so you'll get notified if something breaks.

## Installation

1. Clone the repo

    ```
    https://github.com/bcongdon/travis-build-repeat
    ```

2. Install dependencies

    ```
    pip install -r requirements.txt
    ```

3. Copy `settings.py.template` to `settings.py`.

    ```
    cp settings.py.template settings.py
    ```

4. Create a Github access token [here](https://github.com/settings/tokens) with the following permissions:
    * read:org
    * user:email
    * repo_deployment
    * repo:status
    * write:repo_hook

5. Set `TRAVIS_KEY` in `settings.py` to be this access token.
6. Add the repos you want to keep updated to `TRAVIS_REPOS`, with the format `username/repo_name`
7. Run `zappa deploy` to schedule the AWS Lambda functions. (Note: This will require you to have setup your [AWS credentials file](https://aws.amazon.com/blogs/security/a-new-and-standardized-way-to-manage-credentials-in-the-aws-sdks/))

## Additional Instructions

### Updating

If you make an update to your configuration, run `zappa update` to push those changes to AWS.

### Undeploying

If you want to stop `travis-build-repeat`, run `zappa undeploy` to unschedule the Lambdas.

### Schedule Rate

By default, `travis-build-repeat` runs daily. If you wish to change this rate, edit the event `expression` in `zappa_settings.json`.
You can find a description of valid rate expressions [here](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html).