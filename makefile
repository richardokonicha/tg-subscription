BLACK ?= \033[0;30m
RED ?= \033[0;31m
GREEN ?= \033[0;32m
YELLOW ?= \033[0;33m
BLUE ?= \033[0;34m
PURPLE ?= \033[0;35m
CYAN ?= \033[0;36m
GRAY ?= \033[0;37m
WHITE ?= \033[1;37m
COFF ?= \033[0m

run:
	@echo -e "$(CYAN)Running main:$(COFF)"
	@python main.py


cluster:
	@echo -e "$(CYAN)Create new cluster:$(COFF)"
	@kind create cluster --name development --image kindest/node:v1.23.5

delcluster:
	@echo -e "$(CYAN)delete cluster:$(COFF)"
	@kind delete cluster --name development

apply:
	@kubectl apply -f kubernetes/

setcontext:
	@kubectl cluster-info --context kind-development

kubeconfig:
	@kubectl config

getpods:
	@kubectl get pods

getsvc:
	@kubectl get services

execdocker:
	@docker exec -it development-control-plane bash
# ps auxf

fwdsvc:
	@kubectl port-forward -n tg-subscription svc/tg-subscription 5001:80

dashboard-deploy:
	@kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.6.1/aio/deploy/recommended.yaml

createtoken:
	@kubectl -n kubernetes-dashboard create token admin-user