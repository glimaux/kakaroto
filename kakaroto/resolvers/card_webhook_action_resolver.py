from operations.cards import create_card  # , \
#    update_card, \
#    move_card, \
#    delete_card
# from operations.issues import create_issue


card_webhook_action_resolver = {
    "created": create_card,
    #    "edited": update_card,
    #    "converted": create_issue,
    #    "moved": move_card,
    #    "deleted": delete_card
}
