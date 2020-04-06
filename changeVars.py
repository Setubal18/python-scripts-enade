def updatedVars(list:[]):
    for index in range(len(list)):
        if list[index] == 'cd_catad':
            list.insert(index,' co_categad')
            list.remove('cd_catad')

        elif list[index] == 'cd_orgac':
            list.insert(index,' co_orgacad')
            list.remove('cd_orgac')

        elif list[index] == 'ano_in_gra':
            list.insert(index, ' ano_in_grad')
            list.remove('ano_in_gra')

        elif list[index] == 'tp_semest':
            list.insert(index, ' tp_semestre')
            list.remove('tp_semest')

        elif list[index] == 'status':
            list.insert(index, ' id_status')
            list.remove('status')

        elif list[index] == 'in_grad':
            list.insert(index, 'tp_inscricao')
            list.remove('in_grad')

        elif list[index] == 'nu_que_ofg':
            list.insert(index, ' nu_item_ofg')
            list.remove('nu_que_ofg')

        elif list[index] == 'nu_que_oce':
            list.insert(index, ' nu_item_oce')
            list.remove('nu_que_oce')

        elif list[index] == 'vt_gab_fg':
            list.insert(index, ' ds_vt_gab_ofg_fin')
            list.remove('vt_gab_fg')

        elif list[index] == 'vt_gab_ce':
            list.insert(index, ' ds_vt_gab_oce_fin')
            list.remove('vt_gab_ce')

        elif list[index] == 'vt_esc_ofg':
            list.insert(index, ' ds_vt_esc_ofg')
            list.remove('vt_esc_ofg')

        elif list[index] == 'vt_ace_ofg':
            list.insert(index, ' ds_vt_ace_ofg')
            list.remove('vt_ace_ofg')

        elif list[index] == 'vt_esc_oce':
            list.insert(index, ' ds_vt_esc_oce')
            list.remove('vt_esc_oce')

        elif list[index] == 'vt_ace_oce':
            list.insert(index, ' ds_vt_ace_oce')
            list.remove('vt_ace_oce')
    return list


def lowerVars(keys):
    for i in range(len(keys)):
        new_key = keys[i].lower()
        keys.pop(i)
        keys.insert(i, new_key)
    return keys

