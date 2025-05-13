#
# PySNMP MIB module PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/vla/ArrestedDevelopment/pygwarts/development/filch/mibs/PerfHist-TC-MIB.mib
# Produced by pysmi-0.3.4 at Wed Jul 26 09:25:18 2023
# On host pcfrn3 platform Linux version 5.19.0-50-generic by user vla
# Using Python version 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, IpAddress, ObjectIdentity, ModuleIdentity, Counter64, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, mib_2, iso, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Counter64", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "mib-2", "iso", "TimeTicks", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
perfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 58))
if mibBuilder.loadTexts: perfHistTCMIB.setLastUpdated('9811071100Z')
if mibBuilder.loadTexts: perfHistTCMIB.setOrganization('IETF AToMMIB and TrunkMIB WGs')
if mibBuilder.loadTexts: perfHistTCMIB.setContactInfo('Kaj Tesink Postal: Bellcore 331 Newman Springs Road Red Bank, NJ 07701 USA Tel: +1 732 758 5254 Fax: +1 732 758 2269 E-mail: kaj@bellcore.com')
if mibBuilder.loadTexts: perfHistTCMIB.setDescription('This MIB Module provides Textual Conventions to be used by systems supporting 15 minute based performance history counts.')
class PerfCurrentCount(TextualConvention, Gauge32):
    description = 'A counter associated with a performance measurement in a current 15 minute measurement interval. The value of this counter starts from zero and is increased when associated events occur, until the end of the 15 minute interval. At that time the value of the counter is stored in the first 15 minute history interval, and the CurrentCount is restarted at zero. In the case where the agent has no valid data available for the current interval the corresponding object instance is not available and upon a retrieval request a corresponding error message shall be returned to indicate that this instance does not exist (for example, a noSuchName error for SNMPv1 and a noSuchInstance for SNMPv2 GET operation).'
    status = 'current'

class PerfIntervalCount(TextualConvention, Gauge32):
    description = 'A counter associated with a performance measurement in a previous 15 minute measurement interval. In the case where the agent has no valid data available for a particular interval the corresponding object instance is not available and upon a retrieval request a corresponding error message shall be returned to indicate that this instance does not exist (for example, a noSuchName error for SNMPv1 and a noSuchInstance for SNMPv2 GET operation). In a system supporting a history of n intervals with IntervalCount(1) and IntervalCount(n) the most and least recent intervals respectively, the following applies at the end of a 15 minute interval: - discard the value of IntervalCount(n) - the value of IntervalCount(i) becomes that of IntervalCount(i-1) for n >= i > 1 - the value of IntervalCount(1) becomes that of CurrentCount - the TotalCount, if supported, is adjusted.'
    status = 'current'

class PerfTotalCount(TextualConvention, Gauge32):
    description = 'A counter associated with a performance measurements aggregating the previous valid 15 minute measurement intervals. (Intervals for which no valid data was available are not counted)'
    status = 'current'

mibBuilder.exportSymbols("PerfHist-TC-MIB", PerfTotalCount=PerfTotalCount, perfHistTCMIB=perfHistTCMIB, PYSNMP_MODULE_ID=perfHistTCMIB, PerfCurrentCount=PerfCurrentCount, PerfIntervalCount=PerfIntervalCount)
