grammar = """

    // El axioma inicial
    ?start: exp+

    //Definicion de una expresion
    ?exp: var "=" string "$" -> assignvar
        | var "=" arithmeticoperation "$" -> assignvar
        | var "=" repeat "$" -> assignvar
        | var "=" concat "$" -> assignvar
        | "pantalla" string "$" -> print
        | "pantalla" arithmeticoperation "$" -> print
        | "pantalla" var "$" -> printvar


    // Definicion de operacion aritmetica
    ?arithmeticoperation: product
        | arithmeticoperation "+" product -> add
        | arithmeticoperation "-" product -> sub
    
    ?product: atom
        | product "*" atom -> mul
        | product "/" atom -> div

    ?repeat: "#" number "*" string -> repeat
    
    ?concat: var ":" var-> concat
    
    ?atom: var -> getvar
        | number
        | "-" atom
        | "(" atom ")"
        | "(" var ")"

    ?string: /'[^']*'/
        
    ?var: /[a-zA-Z]\w*/

    ?number: /\d+(\.\d+)?/

    %ignore /\s+/
"""
