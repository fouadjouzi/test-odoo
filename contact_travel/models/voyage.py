from odoo import models, fields, api

class Voyage(models.Model):
    """
    Modèle représentant un voyage effectué par un contact (res.partner).
    Chaque voyage contient un nom, une date de départ, une destination, un montant et un contact associé.
    """
    _name = 'contact.travel.voyage'
    _description = 'Voyage'

    name = fields.Char(string="Nom du voyage", required=True)  # Nom du voyage
    date_depart = fields.Date(string="Date de départ")  # Date de départ du voyage
    destination = fields.Char(string="Destination")  # Destination du voyage
    montant = fields.Float(string="Montant")  # Montant dépensé pour ce voyage
    partner_id = fields.Many2one('res.partner', string="Contact associé")  # Lien vers le contact ayant effectué le voyage

class ResPartner(models.Model):
    """
    Extension du modèle res.partner pour intégrer les voyages associés à chaque contact.
    Ajoute les champs voyage_ids (relation 1-n), voyage_count (calculé), et reward_level (niveau de récompense).
    """
    _inherit = 'res.partner'

    voyage_ids = fields.One2many('contact.travel.voyage', 'partner_id', string="Voyages")  # Liste des voyages du contact
    voyage_count = fields.Integer(string="Nombre de voyages", compute='_compute_voyage_count')  # Nombre de voyages, calculé automatiquement
    reward_level = fields.Selection([
        ('argent', 'Argent'),
        ('or', 'Or'),
        ('platine', 'Platine'),
    ], string="Niveau de récompense", compute="_compute_reward_level", store=True)  # Récompense calculée selon le montant total

    @api.depends('voyage_ids')
    def _compute_voyage_count(self):
        """
        Calcule le nombre de voyages effectués par chaque contact.
        """
        for rec in self:
            rec.voyage_count = len(rec.voyage_ids)

    @api.depends('voyage_ids.montant')
    def _compute_reward_level(self):
        """
        Calcule le niveau de récompense en fonction du total des montants dépensés dans les voyages.
        - Argent : > 0 DA
        - Or : ≥ 50 000 DA
        - Platine : ≥ 100 000 DA
        """
        for rec in self:
            total = sum(v.montant for v in rec.voyage_ids)
            if total >= 100000:
                rec.reward_level = 'platine'
            elif total >= 50000:
                rec.reward_level = 'or'
            elif total > 0:
                rec.reward_level = 'argent'
            else:
                rec.reward_level = False