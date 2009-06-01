typedef struct _f1{
	struct _f1* parent;	//frame pointer - ambiente da função chamante
	void* locals[64];		//espaço de endereçamento para variáveis locais	
	void* outgoing[32];	//espaço de endereçamento para argumentos de funções chamadas
	int return_address;	//endereço do código na função chamante
	void* return_val[32]; //variavel de retorno
}frame;
//Acrescentar aki um return value;
//depois quem chama so tera de aceder a do seu filho:)
