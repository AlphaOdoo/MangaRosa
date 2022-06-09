from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class employee(models.Model):
    _inherit = 'hr.employee'

    sucursal_id = fields.Selection(string='Sucursal',
                                   selection=[('lapaz', 'La Paz'),
                                              ('cbba', 'Cochabamba'),
                                              ('scz', 'Santa Cruz')],
                                   copy=False, default='lapaz')

    # CAmpos Adicionados

    all_name = fields.Char(string='Nombres', required=True, default='')
    paternal_surname = fields.Char(
        string='Apellido Paterno', required=True, default='')
    maternal_surname = fields.Char(
        string='Apellido Materno', required=True, default='')
    maried_surname = fields.Char(
        string='Apellido de Casada', required=True, default='')
    afp_affiliate = fields.Char(
        string='AFP Afiliada', required=True, default='')
    blood_type = fields.Char(string='Tipo de Sangre',
                             required=True, default='')
    cod_laboral = fields.Char(string='Cod. Laboral', required=True, default='')

    @api.onchange('name')
    def _onchange_name(self):
        complete_name = ''

        complete_name = str(self.all_name) + ' ' + \
            str(self.paternal_surname) + ' ' + str(self.maternal_surname)
        self.name = complete_name

    @api.onchange('all_name')
    def _onchange_allname(self):
        complete_name = ''

        complete_name = str(self.all_name) + ' ' + \
            str(self.paternal_surname) + ' ' + str(self.maternal_surname)
        self.name = complete_name

    @api.onchange('paternal_surname')
    def _onchange_pat(self):
        complete_name = ''

        complete_name = str(self.all_name) + ' ' + \
            str(self.paternal_surname) + ' ' + str(self.maternal_surname)
        self.name = complete_name

    @api.onchange('maternal_surname')
    def _onchange_mat(self):
        complete_name = ''

        complete_name = str(self.all_name) + ' ' + \
            str(self.paternal_surname) + ' ' + str(self.maternal_surname)
        self.name = complete_name
