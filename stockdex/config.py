# File for configuration of the stockdex package

from typing import Literal

RESPONSE_TIMEOUT = 2

VALID_SECURITY_TYPES = Literal["stock", "etf", "cryptocurrency", "index", "commodity"]
VALID_DATA_SOURCES = Literal["yahoo_web", "yahoo_api", "justetf", "digrin"]

BASE_URL = "https://query2.finance.yahoo.com/v8/finance"
FUNDAMENTALS_BASE_URL = (
    "https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries"
)
JUSTETF_BASE_URL = "https://www.justetf.com/en"
NASDAQ_BASE_URL = "https://www.nasdaq.com/market-activity/stocks"
DIGRIN_BASE_URL = "https://www.digrin.com/stocks/detail"
MACROTRENDS_BASE_URL = "https://www.macrotrends.net/stocks/charts"

INCOME_STATEMENT_COLUMNS = [
    "TaxEffectOfUnusualItems",
    "TaxRateForCalcs",
    "NormalizedEBITDA",
    "NormalizedDilutedEPS",
    "NormalizedBasicEPS",
    "TotalUnusualItems",
    "TotalUnusualItemsExcludingGoodwill",
    "NetIncomeFromContinuingOperationNetMinorityInterest",
    "ReconciledDepreciation",
    "ReconciledCostOfRevenue",
    "EBITDA",
    "EBIT",
    "NetInterestIncome",
    "InterestExpense",
    "InterestIncome",
    "ContinuingAndDiscontinuedDilutedEPS",
    "ContinuingAndDiscontinuedBasicEPS",
    "NormalizedIncome",
    "NetIncomeFromContinuingAndDiscontinuedOperation",
    "TotalExpenses",
    "RentExpenseSupplemental",
    "ReportedNormalizedDilutedEPS",
    "ReportedNormalizedBasicEPS",
    "TotalOperatingIncomeAsReported",
    "DividendPerShare",
    "DilutedAverageShares",
    "BasicAverageShares",
    "DilutedEPS",
    "DilutedEPSOtherGainsLosses",
    "TaxLossCarryforwardDilutedEPS",
    "DilutedAccountingChange",
    "DilutedExtraordinary",
    "DilutedDiscontinuousOperations",
    "DilutedContinuousOperations",
    "BasicEPS",
    "BasicEPSOtherGainsLosses",
    "TaxLossCarryforwardBasicEPS",
    "BasicAccountingChange",
    "BasicExtraordinary",
    "BasicDiscontinuousOperations",
    "BasicContinuousOperations",
    "DilutedNIAvailtoComStockholders",
    "AverageDilutionEarnings",
    "NetIncomeCommonStockholders",
    "OtherunderPreferredStockDividend",
    "PreferredStockDividends",
    "NetIncome",
    "MinorityInterests",
    "NetIncomeIncludingNoncontrollingInterests",
    "NetIncomeFromTaxLossCarryforward",
    "NetIncomeExtraordinary",
    "NetIncomeDiscontinuousOperations",
    "NetIncomeContinuousOperations",
    "EarningsFromEquityInterestNetOfTax",
    "TaxProvision",
    "PretaxIncome",
    "OtherIncomeExpense",
    "OtherNonOperatingIncomeExpenses",
    "SpecialIncomeCharges",
    "GainOnSaleOfPPE",
    "GainOnSaleOfBusiness",
    "OtherSpecialCharges",
    "WriteOff",
    "ImpairmentOfCapitalAssets",
    "RestructuringAndMergernAcquisition",
    "SecuritiesAmortization",
    "EarningsFromEquityInterest",
    "GainOnSaleOfSecurity",
    "NetNonOperatingInterestIncomeExpense",
    "TotalOtherFinanceCost",
    "InterestExpenseNonOperating",
    "InterestIncomeNonOperating",
    "OperatingIncome",
    "OperatingExpense",
    "OtherOperatingExpenses",
    "OtherTaxes",
    "ProvisionForDoubtfulAccounts",
    "DepreciationAmortizationDepletionIncomeStatement",
    "DepletionIncomeStatement",
    "DepreciationAndAmortizationInIncomeStatement",
    "Amortization",
    "AmortizationOfIntangiblesIncomeStatement",
    "DepreciationIncomeStatement",
    "ResearchAndDevelopment",
    "SellingGeneralAndAdministration",
    "SellingAndMarketingExpense",
    "GeneralAndAdministrativeExpense",
    "OtherGandA",
    "InsuranceAndClaims",
    "RentAndLandingFees",
    "SalariesAndWages",
    "GrossProfit",
    "CostOfRevenue",
    "TotalRevenue",
    "ExciseTaxes",
    "OperatingRevenue",
]

CASH_FLOW_COLUMNS = [
    "ForeignSales",
    "DomesticSales",
    "AdjustedGeographySegmentData",
    "FreeCashFlow",
    "RepurchaseOfCapitalStock",
    "RepaymentOfDebt",
    "IssuanceOfDebt",
    "IssuanceOfCapitalStock",
    "CapitalExpenditure",
    "InterestPaidSupplementalData",
    "IncomeTaxPaidSupplementalData",
    "EndCashPosition",
    "OtherCashAdjustmentOutsideChangeinCash",
    "BeginningCashPosition",
    "EffectOfExchangeRateChanges",
    "ChangesInCash",
    "OtherCashAdjustmentInsideChangeinCash",
    "CashFlowFromDiscontinuedOperation",
    "FinancingCashFlow",
    "CashFromDiscontinuedFinancingActivities",
    "CashFlowFromContinuingFinancingActivities",
    "NetOtherFinancingCharges",
    "InterestPaidCFF",
    "ProceedsFromStockOptionExercised",
    "CashDividendsPaid",
    "PreferredStockDividendPaid",
    "CommonStockDividendPaid",
    "NetPreferredStockIssuance",
    "PreferredStockPayments",
    "PreferredStockIssuance",
    "NetCommonStockIssuance",
    "CommonStockPayments",
    "CommonStockIssuance",
    "NetIssuancePaymentsOfDebt",
    "NetShortTermDebtIssuance",
    "ShortTermDebtPayments",
    "ShortTermDebtIssuance",
    "NetLongTermDebtIssuance",
    "LongTermDebtPayments",
    "LongTermDebtIssuance",
    "InvestingCashFlow",
    "CashFromDiscontinuedInvestingActivities",
    "CashFlowFromContinuingInvestingActivities",
    "NetOtherInvestingChanges",
    "InterestReceivedCFI",
    "DividendsReceivedCFI",
    "NetInvestmentPurchaseAndSale",
    "SaleOfInvestment",
    "PurchaseOfInvestment",
    "NetInvestmentPropertiesPurchaseAndSale",
    "SaleOfInvestmentProperties",
    "PurchaseOfInvestmentProperties",
    "NetBusinessPurchaseAndSale",
    "SaleOfBusiness",
    "PurchaseOfBusiness",
    "NetIntangiblesPurchaseAndSale",
    "SaleOfIntangibles",
    "PurchaseOfIntangibles",
    "NetPPEPurchaseAndSale",
    "SaleOfPPE",
    "PurchaseOfPPE",
    "CapitalExpenditureReported",
    "OperatingCashFlow",
    "CashFromDiscontinuedOperatingActivities",
    "CashFlowFromContinuingOperatingActivities",
    "TaxesRefundPaid",
    "InterestReceivedCFO",
    "InterestPaidCFO",
    "DividendReceivedCFO",
    "DividendPaidCFO",
    "ChangeInWorkingCapital",
    "ChangeInOtherWorkingCapital",
    "ChangeInOtherCurrentLiabilities",
    "ChangeInOtherCurrentAssets",
    "ChangeInPayablesAndAccruedExpense",
    "ChangeInAccruedExpense",
    "ChangeInInterestPayable",
    "ChangeInPayable",
    "ChangeInDividendPayable",
    "ChangeInAccountPayable",
    "ChangeInTaxPayable",
    "ChangeInIncomeTaxPayable",
    "ChangeInPrepaidAssets",
    "ChangeInInventory",
    "ChangeInReceivables",
    "ChangesInAccountReceivables",
    "OtherNonCashItems",
    "ExcessTaxBenefitFromStockBasedCompensation",
    "StockBasedCompensation",
    "UnrealizedGainLossOnInvestmentSecurities",
    "ProvisionandWriteOffofAssets",
    "AssetImpairmentCharge",
    "AmortizationOfSecurities",
    "DeferredTax",
    "DeferredIncomeTax",
    "DepreciationAmortizationDepletion",
    "Depletion",
    "DepreciationAndAmortization",
    "AmortizationCashFlow",
    "AmortizationOfIntangibles",
    "Depreciation",
    "OperatingGainsLosses",
    "PensionAndEmployeeBenefitExpense",
    "EarningsLossesFromEquityInvestments",
    "GainLossOnInvestmentSecurities",
    "NetForeignCurrencyExchangeGainLoss",
    "GainLossOnSaleOfPPE",
    "GainLossOnSaleOfBusiness",
    "NetIncomeFromContinuingOperations",
    "CashFlowsfromusedinOperatingActivitiesDirect",
    "TaxesRefundPaidDirect",
    "InterestReceivedDirect",
    "InterestPaidDirect",
    "DividendsReceivedDirect",
    "DividendsPaidDirect",
    "ClassesofCashPayments",
    "OtherCashPaymentsfromOperatingActivities",
    "PaymentsonBehalfofEmployees",
    "PaymentstoSuppliersforGoodsandServices",
    "ClassesofCashReceiptsfromOperatingActivities",
    "OtherCashReceiptsfromOperatingActivities",
    "ReceiptsfromGovernmentGrants",
    "ReceiptsfromCustomers",
]

BALANCE_SHEET_COLUMNS = [
    "TreasurySharesNumber",
    "PreferredSharesNumber",
    "OrdinarySharesNumber",
    "ShareIssued",
    "NetDebt",
    "TotalDebt",
    "TangibleBookValue",
    "InvestedCapital",
    "WorkingCapital",
    "NetTangibleAssets",
    "CapitalLeaseObligations",
    "CommonStockEquity",
    "PreferredStockEquity",
    "TotalCapitalization",
    "TotalEquityGrossMinorityInterest",
    "MinorityInterest",
    "StockholdersEquity",
    "OtherEquityInterest",
    "GainsLossesNotAffectingRetainedEarnings",
    "OtherEquityAdjustments",
    "FixedAssetsRevaluationReserve",
    "ForeignCurrencyTranslationAdjustments",
    "MinimumPensionLiabilities",
    "UnrealizedGainLoss",
    "TreasuryStock",
    "RetainedEarnings",
    "AdditionalPaidInCapital",
    "CapitalStock",
    "OtherCapitalStock",
    "CommonStock",
    "PreferredStock",
    "TotalPartnershipCapital",
    "GeneralPartnershipCapital",
    "LimitedPartnershipCapital",
    "TotalLiabilitiesNetMinorityInterest",
    "TotalNonCurrentLiabilitiesNetMinorityInterest",
    "OtherNonCurrentLiabilities",
    "LiabilitiesHeldforSaleNonCurrent",
    "RestrictedCommonStock",
    "PreferredSecuritiesOutsideStockEquity",
    "DerivativeProductLiabilities",
    "EmployeeBenefits",
    "NonCurrentPensionAndOtherPostretirementBenefitPlans",
    "NonCurrentAccruedExpenses",
    "DuetoRelatedPartiesNonCurrent",
    "TradeandOtherPayablesNonCurrent",
    "NonCurrentDeferredLiabilities",
    "NonCurrentDeferredRevenue",
    "NonCurrentDeferredTaxesLiabilities",
    "LongTermDebtAndCapitalLeaseObligation",
    "LongTermCapitalLeaseObligation",
    "LongTermDebt",
    "LongTermProvisions",
    "CurrentLiabilities",
    "OtherCurrentLiabilities",
    "CurrentDeferredLiabilities",
    "CurrentDeferredRevenue",
    "CurrentDeferredTaxesLiabilities",
    "CurrentDebtAndCapitalLeaseObligation",
    "CurrentCapitalLeaseObligation",
    "CurrentDebt",
    "OtherCurrentBorrowings",
    "LineOfCredit",
    "CommercialPaper",
    "CurrentNotesPayable",
    "PensionandOtherPostRetirementBenefitPlansCurrent",
    "CurrentProvisions",
    "PayablesAndAccruedExpenses",
    "CurrentAccruedExpenses",
    "InterestPayable",
    "Payables",
    "OtherPayable",
    "DuetoRelatedPartiesCurrent",
    "DividendsPayable",
    "TotalTaxPayable",
    "IncomeTaxPayable",
    "AccountsPayable",
    "TotalAssets",
    "TotalNonCurrentAssets",
    "OtherNonCurrentAssets",
    "DefinedPensionBenefit",
    "NonCurrentPrepaidAssets",
    "NonCurrentDeferredAssets",
    "NonCurrentDeferredTaxesAssets",
    "DuefromRelatedPartiesNonCurrent",
    "NonCurrentNoteReceivables",
    "NonCurrentAccountsReceivable",
    "FinancialAssets",
    "InvestmentsAndAdvances",
    "OtherInvestments",
    "InvestmentinFinancialAssets",
    "HeldToMaturitySecurities",
    "AvailableForSaleSecurities",
    "FinancialAssetsDesignatedasFairValueThroughProfitorLossTotal",
    "TradingSecurities",
    "LongTermEquityInvestment",
    "InvestmentsinJointVenturesatCost",
    "InvestmentsInOtherVenturesUnderEquityMethod",
    "InvestmentsinAssociatesatCost",
    "InvestmentsinSubsidiariesatCost",
    "InvestmentProperties",
    "GoodwillAndOtherIntangibleAssets",
    "OtherIntangibleAssets",
    "Goodwill",
    "NetPPE",
    "AccumulatedDepreciation",
    "GrossPPE",
    "Leases",
    "ConstructionInProgress",
    "OtherProperties",
    "MachineryFurnitureEquipment",
    "BuildingsAndImprovements",
    "LandAndImprovements",
    "Properties",
    "CurrentAssets",
    "OtherCurrentAssets",
    "HedgingAssetsCurrent",
    "AssetsHeldForSaleCurrent",
    "CurrentDeferredAssets",
    "CurrentDeferredTaxesAssets",
    "RestrictedCash",
    "PrepaidAssets",
    "Inventory",
    "InventoriesAdjustmentsAllowances",
    "OtherInventories",
    "FinishedGoods",
    "WorkInProcess",
    "RawMaterials",
    "Receivables",
    "ReceivablesAdjustmentsAllowances",
    "OtherReceivables",
    "DuefromRelatedPartiesCurrent",
    "TaxesReceivable",
    "AccruedInterestReceivable",
    "NotesReceivable",
    "LoansReceivable",
    "AccountsReceivable",
    "AllowanceForDoubtfulAccountsReceivable",
    "GrossAccountsReceivable",
    "CashCashEquivalentsAndShortTermInvestments",
    "OtherShortTermInvestments",
    "CashAndCashEquivalents",
    "CashEquivalents",
    "CashFinancial",
]

FINANCIALS_COLUMNS = [
    "TaxEffectOfUnusualItems",
    "TaxRateForCalcs",
    "NormalizedEBITDA",
    "NormalizedDilutedEPS",
    "NormalizedBasicEPS",
    "TotalUnusualItems",
    "TotalUnusualItemsExcludingGoodwill",
    "NetIncomeFromContinuingOperationNetMinorityInterest",
    "ReconciledDepreciation",
    "ReconciledCostOfRevenue",
    "EBITDA",
    "EBIT",
    "NetInterestIncome",
    "InterestExpense",
    "InterestIncome",
    "ContinuingAndDiscontinuedDilutedEPS",
    "ContinuingAndDiscontinuedBasicEPS",
    "NormalizedIncome",
    "NetIncomeFromContinuingAndDiscontinuedOperation",
    "TotalExpenses",
    "RentExpenseSupplemental",
    "ReportedNormalizedDilutedEPS",
    "ReportedNormalizedBasicEPS",
    "TotalOperatingIncomeAsReported",
    "DividendPerShare",
    "DilutedAverageShares",
    "BasicAverageShares",
    "DilutedEPS",
    "DilutedEPSOtherGainsLosses",
    "TaxLossCarryforwardDilutedEPS",
    "DilutedAccountingChange",
    "DilutedExtraordinary",
    "DilutedDiscontinuousOperations",
    "DilutedContinuousOperations",
    "BasicEPS",
    "BasicEPSOtherGainsLosses",
    "TaxLossCarryforwardBasicEPS",
    "BasicAccountingChange",
    "BasicExtraordinary",
    "BasicDiscontinuousOperations",
    "BasicContinuousOperations",
    "DilutedNIAvailtoComStockholders",
    "AverageDilutionEarnings",
    "NetIncomeCommonStockholders",
    "OtherunderPreferredStockDividend",
    "PreferredStockDividends",
    "NetIncome",
    "MinorityInterests",
    "NetIncomeIncludingNoncontrollingInterests",
    "NetIncomeFromTaxLossCarryforward",
    "NetIncomeExtraordinary",
    "NetIncomeDiscontinuousOperations",
    "NetIncomeContinuousOperations",
    "EarningsFromEquityInterestNetOfTax",
    "TaxProvision",
    "PretaxIncome",
    "OtherIncomeExpense",
    "OtherNonOperatingIncomeExpenses",
    "SpecialIncomeCharges",
    "GainOnSaleOfPPE",
    "GainOnSaleOfBusiness",
    "OtherSpecialCharges",
    "WriteOff",
    "ImpairmentOfCapitalAssets",
    "RestructuringAndMergernAcquisition",
    "SecuritiesAmortization",
    "EarningsFromEquityInterest",
    "GainOnSaleOfSecurity",
    "NetNonOperatingInterestIncomeExpense",
    "TotalOtherFinanceCost",
    "InterestExpenseNonOperating",
    "InterestIncomeNonOperating",
    "OperatingIncome",
    "OperatingExpense",
    "OtherOperatingExpenses",
    "OtherTaxes",
    "ProvisionForDoubtfulAccounts",
    "DepreciationAmortizationDepletionIncomeStatement",
    "DepletionIncomeStatement",
    "DepreciationAndAmortizationInIncomeStatement",
    "Amortization",
    "AmortizationOfIntangiblesIncomeStatement",
    "DepreciationIncomeStatement",
    "ResearchAndDevelopment",
    "SellingGeneralAndAdministration",
    "SellingAndMarketingExpense",
    "GeneralAndAdministrativeExpense",
    "OtherGandA",
    "InsuranceAndClaims",
    "RentAndLandingFees",
    "SalariesAndWages",
    "GrossProfit",
    "CostOfRevenue",
    "TotalRevenue",
    "ExciseTaxes",
    "OperatingRevenue",
]
