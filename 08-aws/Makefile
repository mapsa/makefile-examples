
S3URI = s3://dl-pipeline-storage-prod-refined-bucket/test
AWSPROFILENUMBER = $(shell grep "profile data-scientist" ~/.aws/config | cut -d ':' -f 2 | cut -d ']' -f 1 | cut -d '-'  -f 3)
ACCOUNT_ID = $(shell aws sts get-caller-identity --query Account --output text --profile $(AWS_PROFILE))
AWS_PROFILE=data-scientist-$(AWSPROFILENUMBER)
EXPIRES_IN?=172800

FILE = test.txt

ds-presigned-url: aws-sso
	@echo Generating presigned url for 12 hours
	@aws s3 presign $(S3URI)/$(FILE) \
	--expires-in $(EXPIRES_IN) --profile $(AWS_PROFILE)

aws-sso:
ifneq ($(ACCOUNT_ID), $(AWSPROFILENUMBER))
	$(AWS) sso login --profile $(AWS_PROFILE)
else
	@echo "AWS SSO already logged in"
endif

