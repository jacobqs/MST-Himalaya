import shyft.hydrology as api
import shyft.time_series as sts
from matplotlib import pyplot as plt
#import seaborn as sns

class RadiationRunner():
    def __init__(self):
        self.runner= True


    def run_radiation_ta(self, ta, latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity,
                      flag='instant', rsm=0.0, method='dingman'):

        """Runs radiation model based on the info coming from camels data, with 24 hours timestep """
        # single method test

        # here I will try to reproduce the Fig.1b from Allen2006 (reference)

        # converting station data
        tempP1 = temperature  # [degC], real data should be used
        rhP1 = rhumidity  # [%], real data should be used
        #     rsm = 0.0

        radparam = api.RadiationParameter(albedo, turbidity)
        radcal = api.RadiationCalculator(radparam)
        radres = api.RadiationResponse()

        rv_rso = []  # clear-sky radiation, result vector
        rv_rs = []  # translated, result vector
        rv_ra = []  # extraterrestrial radiation, result vector
        rv_net = []  # net radiation
        rv_net_sw = []  # net short-wave
        rv_net_lw = []  # net long-wave

        # running 24-h timestep
        dayi = 0
        doy = api.DoubleVector()

        # running 24-h timestep
        step = sts.deltahours(24)
        n = ta.size()
        k = 1
        while (k < n):
            time1 = ta.time(k - 1)
            if method == 'dingman':
                radcal.net_radiation_step(radres, latitude_deg, time1, step, slope_deg, aspect_deg,
                                                  tempP1[k], rhP1[k], elevation, rsm[k])
            else:
                radcal.net_radiation_step_asce_st(radres, latitude_deg, time1, step, slope_deg, aspect_deg,
                                                          tempP1[k], rhP1[k], elevation, rsm[k])
            rv_rso.append(radres.sw_t)
            rv_rs.append(radres.sw_cs_p)
            rv_ra.append(radres.ra)
            rv_net.append(radres.net)
            rv_net_sw.append(radres.net_sw)
            rv_net_lw.append(radres.net_lw)
            # print(radres_24h.ra)
            doy.append(dayi)
            k += 1
            dayi += 1
            # doy.append(dayi)

        return doy, rv_ra, rv_rs, rv_rso,rv_net_sw, rv_net_lw, rv_net

    def run_radiation(self, t_start, n, latitude_deg, slope_deg, aspect_deg, elevation, albedo, turbidity, temperature, rhumidity,
                      flag='instant', rsm=0.0, method='dingman'):

        """Module creates shyft radiation model with different timesteps and run it for a defined period of time (1 year with 24-hours averaging) """
        # single method test

        # here I will try to reproduce the Fig.1b from Allen2006 (reference)

        # converting station data
        tempP1 = temperature  # [degC], real data should be used
        rhP1 = rhumidity  # [%], real data should be used
        #     rsm = 0.0

        radparam = api.RadiationParameter(albedo, turbidity)
        radcal_inst = api.RadiationCalculator(radparam)
        radcal_1h = api.RadiationCalculator(radparam)
        radcal_24h = api.RadiationCalculator(radparam)
        radcal_3h = api.RadiationCalculator(radparam)
        radres_inst = api.RadiationResponse()
        radres_1h = api.RadiationResponse()
        radres_24h = api.RadiationResponse()
        radres_3h = api.RadiationResponse()

        rv_rso = []  # clear-sky radiation, result vector
        rv_ra = []  # extraterrestrial radiation, result vector
        rv_net = []  # net radiation
        rv_net_sw = []  # net short-wave
        rv_net_lw = []  # net long-wave

        dayi = 0
        doy = api.DoubleVector()
        # running 24-h timestep
        step = sts.deltahours(24)
        tadays = sts.TimeAxis(t_start, step, n + 1)  # days
        k = 1
        while (k <= n):
            doy.append(dayi)
            k += 1
            dayi += 1

        if flag == '24-hour':
            dayi = 0
            doy = api.DoubleVector()

            # running 24-h timestep
            step = sts.deltahours(24)
            tadays = sts.TimeAxis(t_start, step, n + 1)  # days
            k = 1
            while (k <= n):
                time1 = tadays.time(k - 1)
                if method == 'dingman':
                    radcal_24h.net_radiation_step(radres_24h, latitude_deg, time1, step, slope_deg, aspect_deg,
                                                  tempP1, rhP1, elevation, rsm)
                else:
                    radcal_24h.net_radiation_step_asce_st(radres_24h, latitude_deg, time1, step, slope_deg, aspect_deg,
                                                          tempP1, rhP1, elevation, rsm)
                rv_rso.append(radres_24h.sw_cs_p)
                rv_ra.append(radres_24h.ra)
                rv_net.append(radres_24h.net)
                rv_net_sw.append(radres_24h.net_sw)
                rv_net_lw.append(radres_24h.net_lw)
                # print(radres_24h.ra)
                doy.append(dayi)
                k += 1
                dayi += 1
            # doy.append(dayi)
        elif flag == '3-hour':

            # running 3h timestep
            step = sts.deltahours(3)
            ta3 = sts.TimeAxis(t_start, step, n * 8)  # hours, 1h timestep
            rso_3h = []  # clear-sky radiation
            ra_3h = []  # extraterrestrial radiation
            net_sw_3h = []
            net_lw_3h = []
            net_3h = []
            k = 1
            while (k < n * 8):
                time0 = ta3.time(k - 1)
                if method == 'dingman':
                    radcal_3h.net_radiation_step(radres_3h, latitude_deg, time0, step, slope_deg, aspect_deg, tempP1,
                                                 rhP1, elevation, rsm)
                else:
                    radcal_3h.net_radiation_step_asce_st(radres_3h, latitude_deg, time0, step, slope_deg, aspect_deg,
                                                         tempP1, rhP1, elevation, rsm)
                rso_3h.append(radres_3h.sw_cs_p)
                ra_3h.append(radres_3h.ra)
                net_sw_3h.append(radres_3h.net_sw)
                net_lw_3h.append(radres_3h.net_lw)
                net_3h.append(radres_3h.net)
                k += 1
            rv_rso = [sum(rso_3h[i:i + 8]) for i in range(0, len(rso_3h), 8)]
            rv_ra = [sum(ra_3h[i:i + 8]) for i in range(0, len(ra_3h), 8)]
            rv_net_sw = [sum(net_sw_3h[i:i + 8]) for i in range(0, len(net_sw_3h), 8)]
            rv_net_lw = [sum(net_lw_3h[i:i + 8]) / 8 for i in range(0, len(net_lw_3h), 8)]
            rv_net = [sum(net_3h[i:i + 8]) for i in range(0, len(net_3h), 8)]
        elif flag == '1-hour':
            # runing 1h timestep
            step = sts.deltahours(1)
            ta = sts.TimeAxis(t_start, step, n * 24)  # hours, 1h timestep
            rso_1h = []
            ra_1h = []
            net_sw_1h = []
            net_lw_1h = []
            net_1h = []
            k = 1
            while (k < n * 24):
                time1 = ta.time(k - 1)
                if method == 'dingman':
                    radcal_1h.net_radiation_step(radres_1h, latitude_deg, time1, step, slope_deg, aspect_deg,
                                                 tempP1, rhP1, elevation, rsm)
                else:
                    radcal_1h.net_radiation_step_asce_st(radres_1h, latitude_deg, time1, step, slope_deg, aspect_deg,
                                                         tempP1, rhP1, elevation, rsm)
                rso_1h.append(radres_1h.sw_cs_p)
                ra_1h.append(radres_1h.ra)
                net_sw_1h.append(radres_1h.net_sw)
                net_lw_1h.append(radres_1h.net_lw)
                net_1h.append(radres_1h.net)
                k += 1
            rv_rso = [sum(rso_1h[i:i + 24]) for i in range(0, len(rso_1h), 24)]
            rv_ra = [sum(ra_1h[i:i + 24]) for i in range(0, len(ra_1h), 24)]
            rv_net_sw = [sum(net_sw_1h[i:i + 24]) for i in range(0, len(net_sw_1h), 24)]
            rv_net_lw = [sum(net_lw_1h[i:i + 24]) / 24 for i in range(0, len(net_lw_1h), 24)]
            rv_net = [sum(net_1h[i:i + 24]) for i in range(0, len(net_1h), 24)]
        elif flag == 'instant':
            # running instantaneous with dmin timstep
            minutes = 60
            dmin = 1
            step = sts.deltaminutes(dmin)
            tamin = sts.TimeAxis(t_start, step, n * 24 * minutes)
            rso_inst = []
            ra_inst = []
            net_sw_inst = []
            net_lw_inst = []
            net_inst = []
            doy1 = []
            k = 0
            while (k < n * 24 * minutes):
                timemin = tamin.time(k)
                radcal_inst.net_radiation_inst(radres_inst, latitude_deg, timemin, slope_deg, aspect_deg, tempP1, rhP1,
                                          elevation, rsm)
                rso_inst.append(radres_inst.sw_cs_p)
                ra_inst.append(radres_inst.ra)
                net_sw_inst.append(radres_inst.net_sw)
                net_lw_inst.append(radres_inst.net_lw)
                net_inst.append(radres_inst.net)
                doy1.append(k)
                k += 1
            rv_rso = [sum(rso_inst[i:i + 24 * minutes]) / (24 * minutes) for i in range(0, len(rso_inst), 24 * minutes)]
            rv_ra = [sum(ra_inst[i:i + 24 * minutes]) / (24 * minutes) for i in range(0, len(ra_inst), 24 * minutes)]
            rv_net_sw = [sum(net_sw_inst[i:i + 24 * minutes]) / (24 * minutes) for i in
                         range(0, len(net_sw_inst), 24 * minutes)]
            rv_net_lw = [sum(net_lw_inst[i:i + 24 * minutes]) / (24 * minutes) for i in
                         range(0, len(net_lw_inst), 24 * minutes)]
            rv_net = [sum(net_inst[i:i + 24 * minutes]) / (24 * minutes) for i in range(0, len(net_inst), 24 * minutes)]
        else:
            return 'Nothing todo. Please, specify timestep'

        return doy, rv_ra, rv_rso, rv_net_sw, rv_net_lw, rv_net

