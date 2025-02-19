-- Definindo o nome do arquivo
local b = "arquivo"

-- Se a função lrm_load_script estiver disponível, carregue o script
if lrm_load_script then 
    lrm_load_script(b) 
    while wait(1) do end  -- Espera indefinida (provavelmente uma pausa para o carregamento do script)
end

-- Definindo a URL para obter o script
local c = "https://raw.githubusercontent.com/WillowWillo/SimpleDataBase/refs/heads/master/" .. b .. ".lua"
is_from_loader = {Mode = "fastload"}  -- Configuração para indicar que o script é carregado rapidamente

-- Intervalo de tempo entre operações
local d = 0.03

-- Função para gerenciar o carregamento rápido do script
l_fastload_enabled = function(e)
    -- Caso a operação seja "flush", o script será recarregado
    if e == "flush" then
        wait(d)  -- Aguarda um intervalo de tempo
        d = d + 2  -- Aumenta o intervalo para o próximo carregamento
        local f, g
        local h, i = pcall(function()
            -- Obtém o conteúdo do script da URL
            g = game:HttpGet(c)
            -- Salva o conteúdo obtido em um arquivo de cache
            pcall(writefile, b .. "-cache.lua", "-- " .. a .. "\n\n if not is_from_loader then warn('Use the loadstring, do not run this directly') return end;\n " .. g)
            wait(0.1)  -- Pausa de 0,1 segundo
            -- Tenta carregar o script obtido
            f = loadstring(g)
        end)
        
        -- Caso ocorra algum erro, salva o log de erro e exibe um aviso
        if not h or not f then
            pcall(writefile, "lrm-err-loader-log-httpresp.lua", tostring(g))
            warn("Error while executing loader. Err: " .. tostring(i) .. " See lrm-err-loader-log-httpresp.txt in your workspace.")
            return
        end
        
        -- Executa o script carregado
        f(is_from_loader)
    end

    -- Caso a operação seja "rl", o cache será recarregado
    if e == "rl" then
        pcall(writefile, b .. "-cache.lua", "recache required")
        wait(0.2)
        pcall(delfile, b .. "-cache.lua")  -- Deleta o arquivo de cache anterior
    end
end

l_fastload_enabled("flush")
