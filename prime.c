#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#include<conio.h>
#include<unistd.h>

#define true 1
#define false 0
typedef long long int lint;

int isprime(lint p);
int primefactorization(lint p);
void substitution(int);
void fx(int);
void ph(int n,int q);
void fa(void);
void fxa(int);
void sprime(int);
void syokika(void);

char input[100]={},fixinginput[13]={},pal[10000000][100]={},pa[100]={};
int jo[100]={},num[100]={},pc=0,c=0,k[100]={},flag[100]={},aflag[1000000][13]={};
lint p=0,pl[10000000]={};
lint kmax=pow(10,18),kmin=0,max=0;
int cards,jokerflag=false,fixingflag=false,fixingcards,fixingnumber[13]={},setcards
		,combinationflag=0;

int main(){
	int i,m,j;
	lint s=0;
	char st[100]={};
	while(1){
	syokika();
	printf("êîÇì¸óÕ:");
	scanf("%s",input);
	cards=strlen(input);
	printf("cards=%d\n",cards);
	for(i=0;i<cards;i++){
		if(input[i]=='x'){
			jokerflag=true;
			jo[i]++;
		}else if(input[i]=='a'){
			fixingflag++;
		}
	}
	if(jokerflag==true&&fixingflag==false){
		printf("ñáêîÇéwíË(0Ç≈ëSíTçı):");
		scanf("%d",&setcards);
		if(setcards!=0){
			kmax=pow(10,setcards);
			kmin=pow(10,setcards-1);
		}
	}
	if(fixingflag!=false){
		printf("íËêîÇì¸óÕ:");
		scanf("%s",fixinginput);
		fixingcards=strlen(fixinginput);
		for(i=0;i<fixingcards;i++){
			if(fixinginput[i]=='t'){
				fixingnumber[i]=10;
			}else if(fixinginput[i]=='j'){
				fixingnumber[i]=11;
			}else if(fixinginput[i]=='q'){
				fixingnumber[i]=12;
			}else if(fixinginput[i]=='k'){
				fixingnumber[i]=13;
			}else{
				fixingnumber[i]=fixinginput[i]-'0';
			}
		}
	}
	substitution(cards);
	if(jokerflag==false&&fixingflag==false){
		for(i=0;i<cards;i++){
			if(k[i]<10){
				p*=10;
				p+=k[i];
			}else{
				p*=100;
				p+=k[i];
			}
		}
		if(isprime(p)==true){
			printf("ëfêîÇ‚Ç≈Å[\n");
		}else{
			printf("ëfêîÇ∂Ç·Ç»Ç¢Ç≈Å[\n");
			//primefactorization(p);
		}
		printf("ÇÕÇ¢:1 Ç¢Ç¢Ç¶:2\nëgÇ›çáÇÌÇπÇ‡åvéZÅH:");
		scanf("%d",&combinationflag);
		if(combinationflag==2){
			continue;
		}else{
			ph(cards,cards);
		}
	}else if(fixingflag==false){
		fx(cards);
	}else{
		//fa();
	}
	for(i=0;i<pc;i++){
		for(m=i+1;m<pc;m++){
			if(pl[i]>pl[m]){
				s=pl[i];
				pl[i]=pl[m];
				pl[m]=s;
				strcpy(st,pal[i]);
				strcpy(pal[i],pal[m]);
				strcpy(pal[m],st);
			}
		}
	}
	for(i=0;i<pc;i++){
		//printf("%lld\n",pl[i]);
		printf("%s\n",pal[i]);
	}
	if(jokerflag!=0){
		printf("%då¬\n",c);
		printf("max=%lld",max);
	}
	printf("\n\n");
	}
	return 0;
}

void syokika(void){
	int i,j;
	for(i=0;i<20;i++){
		input[i]='\0';
		k[i]=0;
		jo[i]=0;
		flag[i]=0;
		num[i]=0;
		pa[i]='\0';
	}
	i=0;
	while(pl[i]!=0){
		pl[i]=0;
		for(j=0;j<100;j++){
			pal[i][j]='\0';
		}
		i++;
	}
	pc=0;
	p=0;
	c=0;
	max=0;
	kmax=pow(10,18);
	kmin=0;
	jokerflag=0;
	cards=0;
}

int isprime(lint p){
	lint i;
	if(p==2)return true;
	if(p%2==0)return false;
	for(i=3;i*i<=p;i+=2){
		if(p%i==0){
			return false;
		}
	}
	return true;
}

int primefactorization(lint p){
	lint i,j,copy=p,primefactorcount=0,stock,primefactor[100][2]={};
	for(i=2;i<=p/2;i++){
		if(isprime(i)==true){
			if(p%i==0){
				primefactor[primefactorcount][0]=i;
				for(j=0;;j++){
					copy/=i;
					if(copy%i==0){
						primefactor[primefactorcount][1]++;
					}else{
						break;
					}
				}
				primefactorcount++;
			}
		}
	}
	for(i=0;i<primefactorcount;i++){
		for(j=i+1;j<primefactorcount;j++){
			if(primefactor[i][0]>primefactor[j][0]){
				stock=primefactor[i][0];
				primefactor[i][0]=primefactor[j][0];
				primefactor[j][0]=stock;
			}
		}
	}
	printf("%lld=",p);
	for(i=0;i<primefactorcount-1;i++){
		printf("%lld",primefactor[i][0]);
		if(primefactor[i][1]!=0)printf("^%lld",primefactor[i][1]+1);
		printf("*");
	}
	printf("%lld",primefactor[primefactorcount-1][0]);
	if(primefactor[primefactorcount-1][1]!=0)printf("^%lld",primefactor[primefactorcount-1][1]+1);
	printf("\n");
}

void substitution(int cards){
	int i;
	for(i=0;i<cards;i++){
		if(input[i]=='t'){
			k[i]=10;
		}else if(input[i]=='j'){
			k[i]=11;
		}else if(input[i]=='q'){
			k[i]=12;
		}else if(input[i]=='k'){
			k[i]=13;
		}else if(input[i]=='x'){
			k[i]=14;
		}else if(input[i]=='a'){
			k[i]=15;
		}else{
			k[i]=input[i]-'0';
		}
	}
}

void ad(int n){
	int i;
	for(i=0;i<n;i++){
		//printf("num[i]=%d n=%d\n",num[i],n);
		if(num[i]==10){
			pa[i]='T';
		}else if(num[i]==11){
			pa[i]='J';
		}else if(num[i]==12){
			pa[i]='Q';
		}else if(num[i]==13){
			pa[i]='K';
		}else{
			pa[i]=num[i]+'0';
		}
		//printf("pa[i]=%c\n",pa[i]);
	}
	//for(i=0;i<n;i++){
	strcat(pal[pc],pa);
}

void fx(int n){
	int i,j;
	for(i=0;i<n;i++){
		if(k[i]==14&&jo[i]==1){
			jo[i]=0;
			for(j=1;j<=13;j++){
				num[i]=j;
				fx(n);
				if(j==13){
					jo[i]=1;
					return;
				}
			}
		}else if(k[i]==14){
			continue;
		}else{
			num[i]=k[i];
		}
	}
	for(i=0;i<n;i++){
		if(num[i]<10){
			p*=10;
			p+=num[i];
		}else{
			p*=100;
			p+=num[i];
		}
	}
	if(p<kmax&&p>kmin&&isprime(p)==true){
		if(p>max){
			max=p;
		}
		pl[pc]=p;
		ad(n);
		pc++;
		c++;
	}
	p=0;
	return;
}

void ph(int n,int q){
	int i,j;
	if(q==0){
		p=0;
		for(i=0;i<n;i++){
			if(num[i]<10){
				p*=10;
				p+=num[i];
			}else{
				p*=100;
				p+=num[i];
			}
		}
		if(isprime(p)==true){
			for(i=0;i<pc;i++){
				if(pl[i]==p){
					return;
				}
			}
			if(p>max){
				max=p;
			}
			pl[pc]=p;
			ad(n);
			pc++;
		}
		return;
	}
	for(i=0;i<n;i++){
		if(flag[i]==1)continue;
		flag[i]=1;
		if(k[i]==14){
			for(j=1;j<=13;j++){
				num[q-1]=j;
				ph(n,q-1);
			}
		}else{
			num[q-1]=k[i];
			ph(n,q-1);
		}
		flag[i]=0;
	}
}
