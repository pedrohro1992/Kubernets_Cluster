metadata:
  creationTimestamp: "2021-10-06T22:40:48Z"
  name: pedrohro.com.br
spec:
  api:
    dns: {}
  authorization:
    rbac: {}
  channel: stable
  cloudConfig:
    awsEBSCSIDriver:
      enabled: false
    manageStorageClasses: true
  cloudProvider: aws
  clusterDNSDomain: cluster.local
  configBase: s3://kops-state-b6657/pedrohro.com.br
  configStore: s3://kops-state-b6657/pedrohro.com.br
  containerRuntime: containerd
  containerd:
    configOverride: |
      version = 2

      [plugins]

        [plugins."io.containerd.grpc.v1.cri"]

          [plugins."io.containerd.grpc.v1.cri".cni]
            conf_template = "/etc/containerd/config-cni.template"

          [plugins."io.containerd.grpc.v1.cri".containerd]

            [plugins."io.containerd.grpc.v1.cri".containerd.runtimes]

              [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
                runtime_type = "io.containerd.runc.v2"

                [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
                  SystemdCgroup = true
    logLevel: info
    version: 1.4.9
  dnsZone: pedrohro.com.br
  docker:
    skipInstall: true
  etcdClusters:
  - backups:
      backupStore: s3://kops-state-b6657/pedrohro.com.br/backups/etcd/main
    cpuRequest: 200m
    enableEtcdTLS: true
    enableTLSAuth: true
    etcdMembers:
    - encryptedVolume: true
      instanceGroup: master-us-east-1a
      name: a
    memoryRequest: 100Mi
    name: main
    provider: Manager
    version: 3.4.13
  - backups:
      backupStore: s3://kops-state-b6657/pedrohro.com.br/backups/etcd/events
    cpuRequest: 100m
    enableEtcdTLS: true
    enableTLSAuth: true
    etcdMembers:
    - encryptedVolume: true
      instanceGroup: master-us-east-1a
      name: a
    memoryRequest: 100Mi
    name: events
    provider: Manager
    version: 3.4.13
  iam:
    allowContainerRegistry: true
    legacy: false
  keyStore: s3://kops-state-b6657/pedrohro.com.br/pki
  kubeAPIServer:
    allowPrivileged: true
    anonymousAuth: false
    apiAudiences:
    - kubernetes.svc.default
    apiServerCount: 1
    authorizationMode: Node,RBAC
    bindAddress: 0.0.0.0
    cloudProvider: aws
    enableAdmissionPlugins:
    - NamespaceLifecycle
    - LimitRanger
    - ServiceAccount
    - PersistentVolumeLabel
    - DefaultStorageClass
    - DefaultTolerationSeconds
    - MutatingAdmissionWebhook
    - ValidatingAdmissionWebhook
    - NodeRestriction
    - ResourceQuota
    etcdServers:
    - https://127.0.0.1:4001
    etcdServersOverrides:
    - /events#https://127.0.0.1:4002
    image: k8s.gcr.io/kube-apiserver:v1.21.5
    kubeletPreferredAddressTypes:
    - InternalIP
    - Hostname
    - ExternalIP
    logLevel: 2
    requestheaderAllowedNames:
    - aggregator
    requestheaderExtraHeaderPrefixes:
    - X-Remote-Extra-
    requestheaderGroupHeaders:
    - X-Remote-Group
    requestheaderUsernameHeaders:
    - X-Remote-User
    securePort: 443
    serviceAccountIssuer: https://api.internal.pedrohro.com.br
    serviceAccountJWKSURI: https://api.internal.pedrohro.com.br/openid/v1/jwks
    serviceClusterIPRange: 100.64.0.0/13
    storageBackend: etcd3
  kubeControllerManager:
    allocateNodeCIDRs: true
    attachDetachReconcileSyncPeriod: 1m0s
    cloudProvider: aws
    clusterCIDR: 100.96.0.0/11
    clusterName: pedrohro.com.br
    configureCloudRoutes: true
    image: k8s.gcr.io/kube-controller-manager:v1.21.5
    leaderElection:
      leaderElect: true
    logLevel: 2
    useServiceAccountCredentials: true
  kubeDNS:
    cacheMaxConcurrent: 150
    cacheMaxSize: 1000
    cpuRequest: 100m
    domain: cluster.local
    memoryLimit: 170Mi
    memoryRequest: 70Mi
    nodeLocalDNS:
      cpuRequest: 25m
      enabled: false
      memoryRequest: 5Mi
    provider: CoreDNS
    replicas: 2
    serverIP: 100.64.0.10
  kubeProxy:
    clusterCIDR: 100.96.0.0/11
    cpuRequest: 100m
    hostnameOverride: '@aws'
    image: k8s.gcr.io/kube-proxy:v1.21.5
    logLevel: 2
  kubeScheduler:
    image: k8s.gcr.io/kube-scheduler:v1.21.5
    leaderElection:
      leaderElect: true
    logLevel: 2
  kubelet:
    anonymousAuth: false
    cgroupDriver: systemd
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    hostnameOverride: '@aws'
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    nonMasqueradeCIDR: 100.64.0.0/10
    podManifestPath: /etc/kubernetes/manifests
  kubernetesApiAccess:
  - 0.0.0.0/0
  kubernetesVersion: 1.21.5
  masterInternalName: api.internal.pedrohro.com.br
  masterKubelet:
    anonymousAuth: false
    cgroupDriver: systemd
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    hostnameOverride: '@aws'
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    nonMasqueradeCIDR: 100.64.0.0/10
    podManifestPath: /etc/kubernetes/manifests
    registerSchedulable: false
  masterPublicName: api.pedrohro.com.br
  networkCIDR: 172.20.0.0/16
  networking:
    kubenet: {}
  nonMasqueradeCIDR: 100.64.0.0/10
  secretStore: s3://kops-state-b6657/pedrohro.com.br/secrets
  serviceClusterIPRange: 100.64.0.0/13
  sshAccess:
  - 0.0.0.0/0
  subnets:
  - cidr: 172.20.32.0/19
    name: us-east-1a
    type: Public
    zone: us-east-1a
  topology:
    dns:
      type: Public
    masters: public
    nodes: public
