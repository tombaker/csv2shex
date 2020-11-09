    def _normalize_uripicklist(self):
        """@@@"""
        if self.valueConstraintType == "UriPicklist":
            self.valueConstraint = self.valueConstraint.split()
        return self

