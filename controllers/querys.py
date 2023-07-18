qry_select = """
   select 
   DISTINCT sc.id ,
       CONCAT(sondagem.data, ' ', sondagem.hora) data_venda ,
       iqc.descricao as tabulacao ,
       sondagem.id as id_sondagem ,
       sondagem.ticket_id ,
      
       lc.MUN_NU as ibge ,
       hlr.ddd ,
      
       sondagem.tipo_logradouro ,
       sondagem.logradouro ,
       sondagem.numero ,
       sondagem.bairro ,
       sondagem.cidade ,
       sondagem.estado ,
       sondagem.cep ,
       sondagem.complemento ,
       sondagem.referencia 
     
     from xmodule72.xmodule72_sale_cad sc
     JOIN xmodule72.xmodule72_product_movel_tipo_cad pmt on sc.tipo_plano_id = pmt.id
     JOIN xmodule72.xmodule72_tipo_venda_cad vc on sc.tipo_venda_id = vc.id
     JOIN xmodule72.xmodule72_tipo_conta_cad cc on sc.tipo_conta_id = cc.id
     JOIN xmodule72.xmodule72_forma_pagto_cad fpc on sc.forma_pagto_id = fpc.id
     JOIN xmodule72.xmodule72_sondagem_cad sondagem on sc.sondagem_id = sondagem.id
     LEFT JOIN xmodule72.xmodule72_uf_cad uf_cad on sondagem.uf_orgao_doc = uf_cad.id
     JOIN xmodule72.xmodule72_orgao_emissor_cad oec on sondagem.orgao_emissor_doc = oec.id
     JOIN xmodule72.xmodule72_product_movel_cad pmc on sc.plano_id = pmc.id
     JOIN xcall.icall_queue_class iqc on sondagem.queue_class_id = iqc.id
     JOIN correio.faixa_localidade loc on sondagem.cep BETWEEN loc.LOC_CEP_INI AND loc.LOC_CEP_FIM
     JOIN correio.localidade lc on loc.LOC_NU = lc.LOC_NU
     JOIN xmodule72.xmodule72_documento_cad type_doc on sondagem.documento_id = type_doc.id
     join xmodule72.xmodule72_operadora_doadora_cad oper on operadora_id = oper.id
     LEFT JOIN xmodule72.xmodule72_cidade_ddd_hlr hlr on	lc.MUN_NU = hlr.ibge
     LEFT join xmodule72.xmodule72_classificacao_bo_cad cb1 on sondagem.classificacao_bo_1_id = cb1.id
    WHERE sondagem_id in (4668473,4668798)
   """